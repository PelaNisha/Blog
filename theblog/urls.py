# from django.contrib import admin
from django.urls import path
# from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_details'),
    path('add_Post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
]