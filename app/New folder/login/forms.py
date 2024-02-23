from .models import Account
from django import forms

class LoginForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'password']




