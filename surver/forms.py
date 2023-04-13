from django import forms
from .models import Surver, Category, Channel, Message, Access, Reaction


class SurverForm(forms.ModelForm):

    class Meta:
        model = Surver
        fields = ('name', )


class AccessForm(forms.ModelForm):
    
    class Meta:
        model = Access
        fields = ('user', )


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude = ('surver', )
        

class ChannelForm(forms.ModelForm):

    class Meta:
        model = Channel
        fields = '__all__'


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('content', )


class ReactionForm(forms.ModelForm):

    class Meta:
        model = Reaction
        fields = ('message', )
