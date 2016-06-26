from django.shortcuts import render, get_object_or_404
from news.models import Post, Comment


def index(request):
    posts = Post.objects.all().order_by("-pub_date")
    comments = Comment.objects.all().order_by("-pub_date")[:5]
    context = {'posts': posts, 'comments': comments}
    return render(request, "news/index_bootstrap.html", context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, "news/details_bootstrap.html", context)

