from django.urls import path
from .views import UserRegistrationView, UserEditView, PasswordChangeView, ShowProfilePageView, EditProfilePageView
from . import views

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name= 'register'),
    path('edit_profile/', UserEditView.as_view(), name= 'edit_profile'),
    path('password/', PasswordChangeView.as_view(template_name='registration/change_password.html'), name = 'change_passwprd'),
    path('pass_sucess/', views.password_success, name= 'password_success'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name ='show_profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name ='edit_profile_page'),
    
]
