from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages

from .models import Match
from .forms import MatchForm

class MatchListView(LoginRequiredMixin, ListView):
    model = Match
    template_name = 'list-match.html'
    context_object_name = 'matches'
    permission_required = ('matches.view_match',)  # or 'matches.schedule_match'
    raise_exception = True

class MatchDetailView(LoginRequiredMixin, DetailView):
    model = Match
    template_name = 'details-match.html'
    context_object_name = 'match'
    permission_required = ('matches.view_match',)  # or ('matches.schedule_match',)
    raise_exception = True

class MatchCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Match
    form_class = MatchForm
    template_name = 'create-match.html'
    success_url = reverse_lazy('list-match')
    permission_required = ('matches.add_match', 'matches.schedule_match')
    raise_exception = True

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # <-- pass user to form
        return kwargs

    def form_valid(self, form):
        messages.success(self.request, "Match scheduled.")
        return super().form_valid(form)

class MatchUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Match
    form_class = MatchForm
    template_name = 'edit-match.html'
    success_url = reverse_lazy('list-match')
    permission_required = ('matches.change_match', 'matches.schedule_match')
    raise_exception = True

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # <-- pass user to form
        return kwargs

class MatchDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Match
    template_name = 'delete-match.html'
    success_url = reverse_lazy('list-match')
    permission_required = ('matches.delete_match', 'matches.schedule_match')
    raise_exception = True

    def form_valid(self, form):
        messages.success(self.request, "Match deleted.")
        return super().form_valid(form)