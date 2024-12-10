from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render


from blog.models import BlogPost, Category, Comment
from django.db.models import Q

# Create your views here.

def posts_by_category(request, category_id):
    posts_category = BlogPost.objects.filter(status='Published', category_id=category_id)

    try:
       category = Category.objects.get(pk=category_id)

    except:
        return redirect('home')

    context = {
        'posts_category': posts_category,
        'category': category
    }

    return render(request, 'posts_by_category.html', context)

def blog(request, slug):
    single_blog = get_object_or_404(BlogPost, slug=slug, status='Published')

    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.message = request.POST['message']
        comment.save()
        return HttpResponseRedirect(request.path_info)


    # Comments
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()

    context = {

        'single_blog': single_blog,
        'comments': comments,
        'comment_count': comment_count
    }
    return render(request, 'blog.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    blogs = BlogPost.objects.filter(Q(title__icontains=keyword) | Q(description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')

    context = {
        'blogs': blogs,
        'keyword': keyword
    }
    return render(request, 'search.html', context)
