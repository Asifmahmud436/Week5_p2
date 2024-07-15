from django.shortcuts import render,redirect
from .import forms
from .import models
from django.views.generic import CreateView,UpdateView
from django.urls import reverse_lazy
from django.utils.decorators  import method_decorator
from django.contrib.auth.decorators  import login_required
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib import messages


class AddAuthorView(CreateView):
    model = models.Author
    form_class = forms.AuthorForm
    template_name = 'add_author.html'
    success_url = reverse_lazy('homepage')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
@method_decorator(login_required,name='dispatch')
class EditAuthorView(UpdateView):
    model = models.Author
    form_class = forms.AuthorForm
    template_name = 'add_author.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')

# @method_decorator(login_required,name='dispatch')
class UserLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    def form_valid(self, form):
        return super().form_valid(form)
    def form_invalid(self, form):
        return super().form_invalid(form)
    


    