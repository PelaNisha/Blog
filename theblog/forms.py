from django import forms
from .models import post, Category

choices = Category.objects.all().values_list("name",'name')

choice_list = []
for item in choices:
    choice_list.append(item)



class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ('title', 'title_tag', 'Category','author','body')
        widgets = {
            'title': forms.TextInput(attrs = {'class':'form-control '}),
            'title_tag': forms.TextInput(attrs = {'class':'form-control'}),
            'author': forms.TextInput(attrs = {'class':'form-control', 'value':'','id':'elder','type': 'hidden'}),
            'Category': forms.Select(choices = choice_list, attrs = {'class':'form-control'}),
            'body': forms.Textarea(attrs = {'class':'form-control'}),
        }

class UpdateForm(forms.ModelForm):        
    class Meta:
        model = post
        fields = ('title', 'title_tag','body')
        widgets = {
            'title': forms.TextInput(attrs = {'class':'form-control'}),
            'title_tag': forms.TextInput(attrs = {'class':'form-control'}),
            # 'author': forms.Select(attrs = {'class':'form-control'}),
            'body': forms.Textarea(attrs = {'class':'form-control'}),
        }