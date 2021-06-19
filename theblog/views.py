from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import post
from django.urls import reverse_lazy
# Create your views here.
class HomeView(ListView):
    model = post
    template_name = 'home.html'
    ordering =['-id']

class ArticleDetailView(DetailView):
    model = post
    template_name = 'article_details.html'    


class AddPostView(CreateView):
    model = post
    template_name = 'add_post.html'  
    fields = '__all__'
    

class UpdatePostView(UpdateView):
    model = post
    template_name = 'update_post.html'  
    fields = ['title', 'title_tag', 'body']
        

class DeletePostView(DeleteView):
    model = post
    template_name = 'delete_post.html'  
    success_url = reverse_lazy('home')     