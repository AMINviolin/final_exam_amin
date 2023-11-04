from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import CustomUser
from captcha.fields import CaptchaField

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    image = forms.ImageField()
    id_code = forms.CharField(max_length=11)


    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'email', 'image', 'id_code']

    
class CaptchaForm(forms.Form):
    captcha = CaptchaField()


class AuthenticationForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """

    email = forms.EmailField()
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )