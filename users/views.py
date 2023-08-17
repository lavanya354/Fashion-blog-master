from .forms import ImageUploadForm, UserRegistrationForm
from .models import Image
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm

def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)

def about(request):
    return render(request, 'users/about.html', {'title': 'About'})



def kids(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect('kids')
    else:
        form = ImageUploadForm()
    images = Image.objects.filter(image_type='kids')
    return render(request, 'users/kids.html', {'title': 'Kids', 'images': images, 'form': form})





def men(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect('men')
    else:
        form = ImageUploadForm()
    images = Image.objects.filter(image_type='men')
    return render(request, 'users/men.html', {'title': 'Men', 'images': images, 'form': form})





def women(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect('women')
    else:
        form = ImageUploadForm()
    images = Image.objects.filter(image_type='women')
    return render(request, 'users/women.html', {'title': 'Women', 'images': images, 'form': form})



def post(request):
    return render(request, 'users/post.html', {'title': 'Post'})

def profile(request):
    return render(request, 'users/profile.html', {'title': 'Profile'})