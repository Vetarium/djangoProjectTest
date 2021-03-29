from django.shortcuts import render
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.
def home(request):
    list_posts = Post.objects.all()
    context = {
        'list_posts': list_posts

    }
    template = 'index.html'
    return render(request, template, context)

def login(request):
    context = {

    }
    template = 'login.html'
    return render(request, template, context)

def register(request):
    form = UserCreationForm()
    context = {
        'form' : form
    }
    template = 'register.html'
    return render(request, template, context)