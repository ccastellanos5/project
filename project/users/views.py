from django.shortcuts import render
from .models import User
from django.views.generic import CreateView
from .forms import RegisterForm
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy

def index(request):
    return HttpResponse("Esto es el index")

class UserRegister(CreateView):
    model = User
    template_name = "users/registration/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('index')
