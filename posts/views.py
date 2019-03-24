from django.shortcuts import render
from posts.models import Blog


def index(request):
    blogs = Blog.objects.order_by('-created_datetime')
    return render(request, 'posts/index.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'posts/detail.html', {'blog': blog})

# bootstrap test
def bootstrap(request):
    blogs = Blog.objects.order_by('-created_datetime')
    return render(request, 'posts/bootstrap.html', {'blogs': blogs})

