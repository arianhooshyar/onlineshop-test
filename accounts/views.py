from django.shortcuts import render
from django.views import generic
from .forms import UserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy
from .models import CustomUser


class SignupView(generic.CreateView):
    form_class = UserCreationForm
    model = CustomUser
    success_url = reverse_lazy("login")
    template_name = 'account/signup.html'
