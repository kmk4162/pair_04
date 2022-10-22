from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
  return render(request, 'accounts/index.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {
       'form':form
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def detail(request, pk):
  user = get_user_model().objects.get(pk=pk)
  context = {
    'user':user
  }
  return render(request, 'accounts/detail.html', context)

def login(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        auth_login(request, form.get_user())
        return redirect('reviews:index')
  else:
    form = AuthenticationForm()
  context = {
    'form':form
  }
  return render(request, 'accounts/login.html', context)

def logout(request):
  auth_logout(request)
  return redirect('reviews:index')