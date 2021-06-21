from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import post, Category
from django.urls import reverse_lazy
from .forms import PostForm, UpdateForm
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
    form_class = PostForm
    template_name = 'add_post.html'  
    # fields = '__all__'
    # success_url = reverse_lazy('home')     

class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'  
    fields = '__all__'    

class UpdatePostView(UpdateView):
    model = post
    form_class = UpdateForm
    template_name = 'update_post.html'  
    # fields = ['title', 'title_tag', 'body']
        

class DeletePostView(DeleteView):
    model = post
    template_name = 'delete_post.html'  
    success_url = reverse_lazy('home')     