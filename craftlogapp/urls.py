from django.urls import path
from .views import signupfunc, loginfunc, logoutfunc, detailfunc, detailmfunc, detaildfunc, CraftlogCreate, CraftlogDelete, CraftlogUpdate, combined_list
from . import views

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/',  combined_list, name='list'),
    #path('list/', PictureListView.as_view(), name='list'),
    #path('list/', MovieListView.as_view(), name='list'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('detail_m/<int:pk>', detailmfunc, name='detail_m'),
    path('detail_d/<int:pk>', detaildfunc, name='detail_d'),
    path('create/', CraftlogCreate.as_view(), name='create'),
    path('delete/<int:pk>', CraftlogDelete.as_view(), name='delete'),
    path('update/<int:pk>', CraftlogUpdate.as_view(), name='update'),
]
