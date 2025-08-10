from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

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


class TeamCreateView(LoginRequiredMixin, CreateView):
    model = Team
    form_class = TeamForm
    template_name = 'create-team.html'
    success_url = reverse_lazy('list-team')

    def form_valid(self, form):
        form.instance.coach = self.request.user
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


class TeamDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        team = get_object_or_404(Team, pk=pk)
        if team.coach != request.user:
            messages.error(request, "You can delete only your own team.")
            return redirect('details-team', pk=pk)
        team.delete()
        messages.success(request, "Team deleted.")
        return redirect('list-team')

