from django import forms
from .models import Surver, Category, Channel, Message


class SurverForm(forms.ModelForm):

    class Meta:
        model = Surver
        fields = '__all__'


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'
        

class ChannelForm(forms.ModelForm):

    class Meta:
        model = Channel
        fields = '__all__'


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        exclude = ('reaction', )
