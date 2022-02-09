from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .models import Author, Post, Categories


# Create your views here.

def index(request):
    return render(request, 'index.html')


def author_view(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'author.html', context={'author': author})


def post_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post-details.html', context={'post': post})


def category_view(request, category_id):
    category = get_object_or_404(Categories, pk=category_id)
    posts = Post.objects.filter(category=category).order_by('-reg_date')
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'category.html', context={'category': category, 'page_obj': page_obj})


def login_view(request):
    if request.POST:
        try:
            email = request.POST['email']
            password = request.POST['password']
        except KeyError:
            return render(request, 'login.html', context={'error': "Bad request"})
        user = authenticate(request, username=hash(email.strip()), password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse(author_view))
        else:
            return render(request, 'login.html', context={'error': "Email and password don't matched"})
    return render(request, 'login.html')


def registration(request):
    if request.POST:
        try:
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']
        except KeyError:
            return render(request, 'registration.html', context={'error': 'Something went wrong'})
        if password != password2:
            return render(request, 'registration.html', context={'error': "Passwords don't matched"})
        try:
            user = User.objects.get(username=hash(email.strip()))
        except User.DoesNotExist:
            user = User.objects.create_user(username=hash(email.strip()), email=email, password=password)
            user.save()
            return HttpResponseRedirect(reverse(login_view))
        return render(request, 'registration.html', context={'error': 'Ooops something went wrong'})
    return render(request, 'registration.html')
