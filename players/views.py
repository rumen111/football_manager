from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Player
from .forms import PlayerForm

class PlayerListView(ListView):
    model = Player
    template_name = 'list-player.html'
    context_object_name = 'players'

class PlayerDetailView(DetailView):
    model = Player
    template_name = 'details-player.html'
    context_object_name = 'player'

class PlayerCreateView(LoginRequiredMixin, CreateView):
    model = Player
    form_class = PlayerForm
    template_name = 'create-player.html'
    success_url = reverse_lazy('player-list')

class PlayerUpdateView(LoginRequiredMixin, UpdateView):
    model = Player
    form_class = PlayerForm
    template_name = 'edit-player.html'
    success_url = reverse_lazy('player-list')

class PlayerDeleteView(LoginRequiredMixin, DeleteView):
    model = Player
    template_name = 'delete-player.html'
    success_url = reverse_lazy('player-list')

