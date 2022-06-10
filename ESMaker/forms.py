from django import forms
 

class UserForm(forms.Form):
    name = forms.CharField(label='名前', max_length=100)
    email = forms.EmailField(label='メール', max_length=100)
    password = forms.CharField(max_length=50)