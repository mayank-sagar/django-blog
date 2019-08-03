from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.


def home(request):
    queryset = Post.objects.all()
    context = {
        'posts':queryset
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})