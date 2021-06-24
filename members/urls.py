from django.urls import path
from .views import UserRegistrationView, UserEditView
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name= 'register'),
    path('edit_profile/', UserEditView.as_view(), name= 'edit_profile')
    
]
