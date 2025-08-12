from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Player
from .forms import PlayerForm
from teams.models import Team

class TeamSquadView(LoginRequiredMixin, ListView):
    model = Player
    template_name = 'squad-team.html'
    context_object_name = 'players'

    def get_queryset(self):
        self.team = get_object_or_404(Team, pk=self.kwargs['team_id'])
        # Viewing a squad can be allowed for any authenticated user; no ownership filter here
        return Player.objects.filter(team=self.team).order_by('position', 'name')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['team'] = self.team
        ctx['is_owner'] = (self.request.user == self.team.coach)
        return ctx


class PlayerCreateForTeamView(LoginRequiredMixin, CreateView):
    model = Player
    form_class = PlayerForm
    template_name = 'create-player.html'

    def dispatch(self, request, *args, **kwargs):
        self.team = get_object_or_404(Team, pk=kwargs['team_id'])
        if self.team.coach != request.user:
            messages.error(request, "You can add players only to your own team.")
            return redirect('squad-team', team_id=self.team.pk)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.team = self.team
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('squad-team', kwargs={'team_id': self.team.pk})

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['team'] = self.team
        return ctx


class PlayerUpdateView(LoginRequiredMixin, UpdateView):
    model = Player
    form_class = PlayerForm
    template_name = 'edit-player.html'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.team.coach != request.user:
            messages.error(request, "You can edit players only in your own team.")
            return redirect('squad-team', team_id=self.object.team_id)
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('squad-team', kwargs={'team_id': self.object.team_id})


class PlayerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Player
    template_name = 'delete-player.html'  # confirmation page

    def test_func(self):
        # Only the coach of the player's team can delete
        return self.get_object().team.coach == self.request.user

    def get_success_url(self):
        team_id = self.object.team_id
        messages.success(self.request, "Player deleted.")
        return reverse('squad-team', kwargs={'team_id': team_id})