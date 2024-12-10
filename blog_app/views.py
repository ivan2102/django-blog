from django.shortcuts import redirect, render
from django.contrib import auth
from about.models import About
from blog.models import BlogPost, Category
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    categories = Category.objects.all()
    featured_posts = BlogPost.objects.filter(is_featured=True, status='Published')
    posts = BlogPost.objects.filter(is_featured=False, status='Published')

    try:

        about = About.objects.get()

    except:
        about = None

    context = {
        'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about
    }
    return render(request, 'home.html', context)

def register(request):

    if request.method == 'POST':
         form = RegistrationForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('home')
    else:
     form = RegistrationForm()

    context = {

        'form': form
    }
    return render(request, 'register.html', context)

def login(request):
    if request.method == 'POST':

     form = AuthenticationForm(request, request.POST)
     if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
           auth.login(request, user)
        return redirect('dashboard')

    else:
       form = AuthenticationForm
    
    context = {
        'form': form
    }
    
    return render(request, 'login.html', context)

def logout(request):
   auth.logout(request)
   return redirect('home')