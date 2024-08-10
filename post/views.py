from django.shortcuts import render
from .forms import CreatePostForm


def test(request):
    return render(request, 'test.html')


def create_post(request):
    context = dict()
    context['form'] = CreatePostForm()
    form = CreatePostForm(request.POST or None)

    if form.is_valid():
        form.save()
        # print("Form Was Added")

    context['form'] = form

    return render(request, 'add_posts.html', {"form": CreatePostForm()})
