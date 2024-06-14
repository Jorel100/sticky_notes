from django.shortcuts import render, get_object_or_404, redirect
from .models import BulletinPost
from .forms import BulletinPostForm


def bulletin_post_list(request):
    posts = BulletinPost.objects.all()
    return render(request, 'bulletin/post_list.html', {'posts': posts})


def bulletin_post_detail(request, pk):
    post = get_object_or_404(BulletinPost, pk=pk)
    return render(request, 'bulletin/post_detail.html', {'post': post})


def bulletin_post_new(request):
    if request.method == "POST":
        form = BulletinPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('bulletin_post_detail', pk=post.pk)
    else:
        form = BulletinPostForm()
    return render(request, 'bulletin/post_edit.html', {'form': form})


def bulletin_post_edit(request, pk):
    post = get_object_or_404(BulletinPost, pk=pk)
    if request.method == "POST":
        form = BulletinPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('bulletin_post_detail', pk=post.pk)
    else:
        form = BulletinPostForm(instance=post)
    return render(request, 'bulletin/post_edit.html', {'form': form})
