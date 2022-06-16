from django import forms
from .models import User


class UserForm(forms.ModelForm):
    # name = forms.CharField(label='名前', max_length=100)
    # email = forms.EmailField(label='メール', max_length=100)
    # password = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ("name", "email", "password",)
