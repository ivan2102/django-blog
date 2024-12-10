from django.urls import path

from . import views

urlpatterns = [

  path('', views.dashboard, name='dashboard'),
  #category crud
  path('category/', views.category, name='category'),
  path('add_category/', views.add_category, name='add_category'),
  path('edit_category/<int:pk>/', views.edit_category, name='edit_category'),
  path('delete_category/<int:pk>/', views.delete_category, name='delete_category'),
  # posts crud
  path('posts/', views.posts, name='posts'),
  path('add_post/', views.add_post, name='add_post'),
  path('edit_post/<int:pk>/', views.edit_post, name='edit_post'),
  path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
  #users
  path('users/', views.users, name='users'),
  path('add_user/', views.add_user, name='add_user'),
  path('edit_user/<int:pk>/', views.edit_user, name='edit_user'),
  path('delete_user/<int:pk>/', views.delete_user, name='delete_user'),
  path('logout/', views.logout, name='logout'),
]
