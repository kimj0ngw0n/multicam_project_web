from django import forms
from .models import Surver, Category, Channel, Message, Access


class SurverForm(forms.ModelForm):

    class Meta:
        model = Surver
        fields = '__all__'


class AccessForm(forms.ModelForm):
    
    class Meta:
        model = Access
        exclude = ('surver', )


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude = ('surver', )
        

class ChannelForm(forms.ModelForm):

    class Meta:
        model = Channel
        exclude = ('category', )


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('content', )
