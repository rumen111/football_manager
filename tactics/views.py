from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Tactic
from .forms import TacticForm
from accounts.models import Profile

class TacticListView(LoginRequiredMixin, ListView):
    model = Tactic
    template_name = 'list-tactic.html'
    context_object_name = 'tactics'

    def get_queryset(self):
        # Only my tactics (User -> Profile via created_by__user)
        return Tactic.objects.filter(created_by__user=self.request.user)

class TacticDetailView(LoginRequiredMixin, DetailView):
    model = Tactic
    template_name = 'details-tactic.html'
    context_object_name = 'tactic'

    def get_queryset(self):
        return Tactic.objects.filter(created_by__user=self.request.user)

class TacticCreateView(LoginRequiredMixin, CreateView):
    model = Tactic
    form_class = TacticForm
    template_name = 'create-tactic.html'
    success_url = reverse_lazy('list-tactic')

    def form_valid(self, form):
        # Attach the current user's Profile (create it if somehow missing)
        profile, _ = Profile.objects.get_or_create(user=self.request.user)
        form.instance.created_by = profile
        return super().form_valid(form)

class TacticUpdateView(LoginRequiredMixin, UpdateView):
    model = Tactic
    form_class = TacticForm
    template_name = 'edit-tactic.html'
    success_url = reverse_lazy('list-tactic')

    def get_queryset(self):
        # Only allow editing your own tactics
        return Tactic.objects.filter(created_by__user=self.request.user)

class TacticDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        # Only allow deleting your own tactics
        tactic = get_object_or_404(Tactic, pk=pk, created_by__user=request.user)
        tactic.delete()
        messages.success(request, "Tactic deleted.")
        return redirect('list-tactic')