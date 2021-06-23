from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import post, Category
from django.urls import reverse_lazy, reverse
from .forms import PostForm, UpdateForm
from django.http import HttpResponseRedirect
# Create your views here.

def LikeView(request , pk):
    Post = get_object_or_404(post, id=request.POST.get('post_id'))
    liked = False
    if Post.likes.filter(id= request.user.id).exists():
        Post.likes.remove(request.user)
        liked = False
    else:
        Post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article_details', args = [str(pk)]))


class HomeView(ListView):
    model = post
    template_name = 'home.html'
    ordering =['-id']

class ArticleDetailView(DetailView):
    model = post
    template_name = 'article_details.html'    


    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args,**kwargs)
        
        stuff = get_object_or_404(post, id = self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id  =self.request.user.id).exists():
            liked = True
        context['total_likes'] = total_likes
        context['cat_menu'] = cat_menu
        context['liked'] = liked
        return context


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

def CategoryView(request , cats):
    category_posts = post.objects.filter(Category = cats.replace('-', ''))
    return render(request, 'categories.html',{'cats':cats.title().replace('-', ''), 'category_posts':category_posts})

def CategoryListView(request ):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html',{'cat_menu_list':cat_menu_list})



class UpdatePostView(UpdateView):
    model = post
    form_class = UpdateForm
    template_name = 'update_post.html'  
    # fields = ['title', 'title_tag', 'body']
        

class DeletePostView(DeleteView):
    model = post
    template_name = 'delete_post.html'  
    success_url = reverse_lazy('home')     