from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Favorite
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User



# Create your views here.

def home(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'blogs': blogs})

@login_required
def detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blog/detail.html', {'blog': blog})

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            send_mail(
                'New Blog Created',
                'A new blog has been created.',
                'from@example.com',
                [user.email for user in User.objects.all()],
                fail_silently=False,
            )
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'blog/create_blog.html', {'form': form})

@login_required
def update_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/update_blog.html', {'form': form})

@login_required
def delete_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        blog.delete()
        return redirect('home')
    return render(request, 'blog/delete_blog.html', {'blog': blog})

@login_required
def add_to_favorites(request, id):
    blog = get_object_or_404(Blog, id=id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, blog=blog)
    return redirect('home')

@login_required
def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog-home')
    return render(request, 'blog/delete_blog.html', {'blog': blog})