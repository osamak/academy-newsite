from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from news.models import Post

def index(request):
    posts = Post.objects.all().order_by("-pub_date")
    context = {'posts': posts}
    return render(request, "news/index.html", context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, "news/details.html", context)

