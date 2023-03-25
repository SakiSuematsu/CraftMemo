from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import CraftlogModel
from django.views.generic import CreateView
from django.urls import reverse_lazy


# Create your views here.


def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, 'signup.html', {'some': 100})
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーはすでに登録されています'})
    return render(request, 'signup.html')


def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})


def picturelistfunc(request):
    object_list = CraftlogModel.objects.filter(filetype='picture')
    return render(request, 'list.html', {'object_list': object_list})


def movielistfunc(request):
    movie_list = CraftlogModel.objects.filter(filetype='movie')
    return render(request, 'list.html', {'movie_list': movie_list})


def logoutfunc(request):
    logout(request)
    return redirect('login')


def detailfunc(request, pk):
    object = get_object_or_404(CraftlogModel, pk=pk)
    return render(request, 'detail.html', {'object': object})


class CraftlogCreate(CreateView):
    template_name = 'create.html'
    model = CraftlogModel
    fields = ('title', 'content', 'author', 'filetype', 'craftimage')
    success_url = reverse_lazy('list')
