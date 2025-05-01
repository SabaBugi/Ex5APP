from django.shortcuts import render
from .forms import UserRegistrationForm, CategoryForm
from django.contrib import messages

def home_view(request):
    return render(request, 'Ex1App/home.html')

def user_registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data
            messages.success(request, 'User registered successfully!')
    else:
        form = UserRegistrationForm()
    return render(request, 'Ex1App/user_registration.html', {'form': form})

def category_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully!')
    else:
        form = CategoryForm()
    return render(request, 'Ex1App/category.html', {'form': form})