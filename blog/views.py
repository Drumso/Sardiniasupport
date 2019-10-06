from django.shortcuts import render

from markdownx.utils import markdownify

from .models import Post, Comment, Category, RecipePost
from .forms import CommentForm

def recipe_post_index(request):
    posts = RecipePost.objects.all().order_by("-created_on")
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


def recipe_category(request, category):
    posts = Post.objects.filter(
        categories__name__exact=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog/category.html", context)


def recipe_post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
    context = {
        'post': post,
        'post_body': markdownify(post.body),
        "comments": comments,
        "form": form,
    }
    return render(request, 'blog/detail.html', context)