from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from.models import Post, Novo, Mensage
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())\
        .order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
def projeto(request):
    return render(request, 'blog/projeto.html', {})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def novo_list(request):
    posts = Novo.objects.filter(published_date__lte=timezone.now())\
        .order_by('published_date')
    return render(request, 'blog/novo_list.html', {'post': posts})

def novo_detail(request, pk):
    post = get_object_or_404(Novo, pk=pk)
    return render(request, 'blog/novo_detail.html', {'post': post})
def novo_edit(request, pk):
    post = get_object_or_404(Novo, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/novo_edit.html', {'form': form})


def mensage_list(request):
    posts = Mensage.objects.filter(published_date__lte=timezone.now())\
        .order_by('published_date')
    return render(request, 'blog/mensage_list.html', {'post': posts})

def mensage_detail(request, pk):
    post = get_object_or_404(Mensage, pk=pk)
    return render(request, 'blog/mensage_detail.html', {'post': post})
def mensage_edit(request, pk):
    post = get_object_or_404(Mensage, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/mensage_edit.html', {'form': form})


