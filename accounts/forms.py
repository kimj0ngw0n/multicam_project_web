from django import forms
from .models import Access
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', )


class AccessForm(forms.ModelForm):
    
    class Meta:
        model = Access
        fields = '__all__'
