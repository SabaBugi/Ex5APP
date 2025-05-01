from django import forms
from .models import Category

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'is_active']
