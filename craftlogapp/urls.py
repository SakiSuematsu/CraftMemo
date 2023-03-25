from django.urls import path
from .views import signupfunc, loginfunc, logoutfunc, detailfunc, CraftlogCreate, picturelistfunc

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', picturelistfunc, name='list'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('create/', CraftlogCreate.as_view(), name='create'),
]
