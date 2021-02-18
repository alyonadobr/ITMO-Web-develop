from django.db import transaction
from django.shortcuts import render
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, View
from django.contrib.auth import authenticate, login
from .forms import  LoginForm



class BaseView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')




























class LoginView(BaseView, View):
    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)

        context = {'form': form,  'cart':self.cart}
        return render(request, 'render.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')
            return render(request, 'index.html', {'form': form, 'cart': self.cart})

