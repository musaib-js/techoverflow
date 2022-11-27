from django.shortcuts import render
from .models import Post

def index(request):
    toppost = Post.objects.all().order_by('-time_stamp')[0]
    posts = Post.objects.filter().order_by('-time_stamp')[0:3]
    allposts = Post.objects.filter().order_by('-time_stamp')
    popularposts = Post.objects.all()[0:3]
    context = {'toppost': toppost, 'posts':posts, 'allposts': allposts, 'popularposts': popularposts }
    return render(request, 'index.html', context)

def post(request, id):
    post = Post.objects.filter(id = id)[0]
    related_posts = Post.objects.filter(category = post.category and id!=post.id)
    context = {'post':post, 'related_posts':related_posts}
    return render(request, 'article.html', context)

def category(request, category):
    post = Post.objects.filter(category = category)
    print(post)
    context = {'post':post}
    return render(request, 'category.html', context)