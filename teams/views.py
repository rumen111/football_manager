from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from players.models import Player
from .models import Team
from .forms import TeamForm


class TeamListView(ListView):
    model = Team
    template_name = 'list-team.html'
    context_object_name = 'teams'


class TeamDetailView(DetailView):
    model = Team
    template_name = 'details-team.html'
    context_object_name = 'team'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team = self.object
        context['player_count'] = Player.objects.filter(team=team).count()
        return context


class TeamCreateView(LoginRequiredMixin, CreateView):
    model = Team
    fields = ['name', 'city', 'founded_year', 'logo']
    template_name = 'create-team.html'
    success_url = reverse_lazy('list-team')

    def form_valid(self, form):
        form.instance.coach = self.request.user
        if Team.objects.filter(coach=self.request.user).count() >= 2:
            form.add_error(None, "You cannot create more than 2 teams.")
            return self.form_invalid(form)
        return super().form_valid(form)


class TeamUpdateView(LoginRequiredMixin, UpdateView):
    model = Team
    form_class = TeamForm
    template_name = 'edit-team.html'
    success_url = reverse_lazy('list-team')

    # simple ownership enforcement
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.coach != request.user:
            messages.error(request, "You can edit only your own team.")
            return redirect('details-team', pk=obj.pk)
        return super().dispatch(request, *args, **kwargs)


class TeamDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Team
    template_name = 'delete-team.html'  # The confirmation template
    success_url = reverse_lazy('list-team')

    def test_func(self):
        # Only allow deletion if current user is the coach
        return self.get_object().coach == self.request.user

