from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Match
from .forms import MatchForm

class MatchListView(LoginRequiredMixin, ListView):
    model = Match
    template_name = 'list-match.html'
    context_object_name = 'matches'

    def get_queryset(self):
        u = self.request.user
        return Match.objects.filter(Q(home_team__coach=u) | Q(away_team__coach=u)).select_related(
            'home_team', 'away_team'
        )

class MatchDetailView(LoginRequiredMixin, DetailView):
    model = Match
    template_name = 'details-match.html'
    context_object_name = 'match'

    def get_queryset(self):
        u = self.request.user
        return Match.objects.filter(Q(home_team__coach=u) | Q(away_team__coach=u)).select_related(
            'home_team', 'away_team'
        )

class MatchCreateView(LoginRequiredMixin, CreateView):
    model = Match
    form_class = MatchForm
    template_name = 'create-match.html'
    success_url = reverse_lazy('list-match')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class MatchUpdateView(LoginRequiredMixin, UpdateView):
    model = Match
    form_class = MatchForm
    template_name = 'edit-match.html'
    success_url = reverse_lazy('list-match')

    def get_queryset(self):
        u = self.request.user
        return Match.objects.filter(Q(home_team__coach=u) | Q(away_team__coach=u))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class MatchDeleteView(LoginRequiredMixin, View):
    """POST-only delete (no confirm page)."""
    def post(self, request, pk):
        u = request.user
        match = get_object_or_404(Match, pk=pk)
        if match.home_team.coach != u and match.away_team.coach != u:
            messages.error(request, "You can delete only your own matches.")
            return redirect('details-match', pk=pk)
        match.delete()
        messages.success(request, "Match deleted.")
        return redirect('list-match')