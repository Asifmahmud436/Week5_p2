from django.shortcuts import render,redirect
from .import forms
from .import models
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.utils.decorators  import method_decorator
from django.contrib.auth.decorators  import login_required


class AddPostView(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('homepage')
    def form_valid(self, form):
        form.instance.album = self.request.user
        return super().form_valid(form)

class EditAlbumView(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')

class DeleteAlbumView(DeleteView):
    model = models.Album
    template_name = 'delete_album.html'
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = 'id'

    