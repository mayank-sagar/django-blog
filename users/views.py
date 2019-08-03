from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    form = UserRegisterForm()
    if request.method.upper() == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request,f'{username} account is created now log in!')
            form.save()
            return redirect('blog-login')
    context = {
        
        'form':form
    }
    return render(request,'users/register.html',context)

@login_required
def profile(request):
    return render(request,'users/profile.html')