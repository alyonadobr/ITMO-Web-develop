from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):

        password = forms.CharField(widget=forms.PasswordInput)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].label = 'Логин'
            self.fields['password'].label = 'Пароль'


        class Meta:
          model = User
          fields = ['username', 'password']
