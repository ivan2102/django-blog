from django import forms
from blog.models import BlogPost, Category
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AddCategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = '__all__' 


class PostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('title', 'category', 'featured_image', 'description', 'blog_body', 'status', 'is_featured')

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'is_active', 'groups', 'user_permissions')


class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'is_active', 'groups', 'user_permissions')
