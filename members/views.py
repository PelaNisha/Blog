from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm
from django.views.generic import DetailView
from theblog.models import Profile

# Create your views here.
class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    # profile = get_object_or_404(profile, id=request.POST.get('user.id'))
    
    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView,self).get_context_data(*args,**kwargs)
        page_user = get_object_or_404(Profile, id = self.kwargs['pk'])
        context['page_user'] = page_user
        return context


class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    # template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password-success')



def password_success(request):
    return render(request, 'registration/password_success.html',{})


class UserRegistrationView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')


    def get_object(self):
        return self.request.user



