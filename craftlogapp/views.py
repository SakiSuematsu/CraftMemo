from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import CraftlogModel
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.views import View

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

def combined_list(request):
    object_list = CraftlogModel.objects.filter(filetype__in=['picture', 'movie', '3d'],author=request.user)
    context = {
        'picture_list': object_list.filter(filetype='picture',author=request.user),
        'movie_list': object_list.filter(filetype='movie',author=request.user),
        'threed_list': object_list.filter(filetype='3d',author=request.user),
    }
    return render(request, 'list.html', context)


def logoutfunc(request):
    logout(request)
    return redirect('login')


def detailfunc(request, pk):
    object = get_object_or_404(CraftlogModel, pk=pk)
    return render(request, 'detail.html', {'object': object})

def detailmfunc(request, pk):
    object = get_object_or_404(CraftlogModel, pk=pk)
    return render(request, 'detail_m.html', {'object': object})

def detaildfunc(request, pk):
    object = get_object_or_404(CraftlogModel, pk=pk)
    return render(request, 'detail_d.html', {'object': object})

class CraftlogCreate(CreateView):
    template_name = 'create.html'
    model = CraftlogModel
    fields = ('title', 'content', 'author', 'filetype', 'storage', 'craftimage')
    success_url = reverse_lazy('list')

class CraftlogDelete(DeleteView):
    template_name = 'delete.html'
    model = CraftlogModel
    success_url = reverse_lazy('list')

class CraftlogDeleteM(DeleteView):
    template_name = 'delete_m.html'
    model = CraftlogModel
    success_url = reverse_lazy('list')

class CraftlogDeleteD(DeleteView):
    template_name = 'delete_d.html'
    model = CraftlogModel
    success_url = reverse_lazy('list')

class CraftlogUpdate(UpdateView):
    template_name = 'update.html'
    model = CraftlogModel
    fields = ('title', 'content', 'author', 'filetype', 'storage', 'craftimage')
    success_url = reverse_lazy('list')