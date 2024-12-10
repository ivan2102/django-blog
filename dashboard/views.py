from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from blog.models import BlogPost, Category
from .forms import AddCategoryForm, EditUserForm, PostForm, UserForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = BlogPost.objects.all().count()

    context = {
        'category_count': category_count,
        'blogs_count': blogs_count
    }
    return render(request, 'dashboard/dashboard.html', context)


def category(request):
    category = Category.objects.all()

    context = {
        'category': category
    }

    return render(request, 'dashboard/dashboard_category.html', context)

def add_category(request):

    if request.method == 'POST':

     form = AddCategoryForm(request.POST)

     if form.is_valid():
         form.save()
         return redirect('category')

    context = {
        'form': form
    }
    return render(request, 'dashboard/add_category.html', context)

def edit_category(request, pk):

    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':

        form = AddCategoryForm(request.POST, instance=category)

        if form.is_valid():
            form.save()
            return redirect('category')

    form = AddCategoryForm(instance=category)

    context = {
        'form': form,
        'category': category
    }
    return render(request, 'dashboard/edit_category.html', context)

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('category')

def posts(request):

    posts = BlogPost.objects.all()

    context = {
        'posts': posts,
        
    }
    return render(request, 'dashboard/posts.html', context)

def add_post(request):

    if request.method == 'POST':

        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts')

    form = PostForm()

    context = {
        'form': form
    }

    return render(request, 'dashboard/add_post.html', context)

def edit_post(request, pk):

    post = get_object_or_404(BlogPost, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
         post = form.save()
         title = form.cleaned_data['title']
         post.slug = slugify(title) + '-' + str(post.id)
         post.save()
        return redirect('posts')
    
    form = PostForm(instance=post)

    context = {
        'post': post,
        'form': form
    }
    return render(request, 'dashboard/edit_post.html', context)

def delete_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    post.delete()
    return redirect('posts')

# Users
def users(request):
    
    users = User.objects.all()

    context = {
        'users': users,
        
    }
    return render(request, 'dashboard/users.html', context)

def add_user(request):
    if request.method == 'POST':
       form = UserForm(request.POST)
       if form.is_valid():
          form.save()
          return redirect('users')
    
    form = UserForm()
        
    context = {
        'form': form
    }

    
    return render(request, 'dashboard/add_user.html', context)


def edit_user(request, pk):

    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
        
    form = EditUserForm(instance=user)

    context = {
        'user': user,
        'form': form
    }
    return render(request, 'dashboard/edit_user.html', context)

def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('users')

def logout(request):
    pass
