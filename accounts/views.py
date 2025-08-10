from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User

from accounts.forms import RegisterForm
from accounts.models import Profile


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('dashboard')  # Redirect after registration

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)  # auto-login after register
        return response

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['email'].required = True  # Add email field manually
        return form


from django.shortcuts import render

# Create your views here.
