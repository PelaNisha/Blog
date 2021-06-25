from django.urls import path
from .views import UserRegistrationView, UserEditView, PasswordChangeView
from . import views

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name= 'register'),
    path('edit_profile/', UserEditView.as_view(), name= 'edit_profile'),
    path('password/', PasswordChangeView.as_view(template_name='registration/change_password.html'), name = 'change_passwprd'),
    path('pass_sucess/', views.password_success, name= 'password_success'),
    
]
