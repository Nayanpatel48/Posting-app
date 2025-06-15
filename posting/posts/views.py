from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, PostForm
from .models import Post

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('posts:home')
    return render(request, 'posts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('posts:home')
        messages.error(request, 'Invalid credentials')
    return render(request, 'posts/login.html')

def logout_view(request):
    logout(request)
    return redirect('posts:login')

@login_required
def home(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'posts/home.html', {'posts': posts})

@login_required
def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        p = form.save(commit=False)
        p.author = request.user
        p.save()
        return redirect('posts:home')
    return render(request, 'posts/post_form.html', {'form': form})

@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('posts:home')
    return render(request, 'posts/post_form.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('posts:home')
    return render(request, 'posts/confirm_delete.html', {'post': post})