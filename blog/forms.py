from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post, Coments, Mailing, UserProfile


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('published_date', 'user',)


class ComentsForm(forms.ModelForm):
    class Meta:
        model = Coments
        exclude = ('coment_date', 'post_id', 'user',)
        fields = ['coment']  # Одне поле - coment
        widgets = {
            'coment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['email']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'description']
