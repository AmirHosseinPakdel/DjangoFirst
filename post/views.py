from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreatePostForm
from .models import Post
from django.urls import reverse

from .models import Post


def home(request):
    return render(request, 'home.html', {"posts": Post.objects.all()})


def delete(request, post_id):
    obj = get_object_or_404(Post, id=post_id)
    obj.delete()
    print("Post was deleted!")
    return redirect("home")


def create_post(request):
    context = dict()
    context['form'] = CreatePostForm()
    form = CreatePostForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect("home")

    context['form'] = form

    return render(request, 'add_posts.html', {"form": CreatePostForm()})
