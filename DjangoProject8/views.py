from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from teams.models import Team
from matches.models import Match
from tactics.models import Tactic

class IndexView(TemplateView):
    template_name = 'index.html'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        u = self.request.user
        ctx['my_teams'] = Team.objects.filter(coach=u).prefetch_related('players')
        ctx['my_matches'] = (
            Match.objects
            .filter(home_team__coach=u) | Match.objects.filter(away_team__coach=u)
        ).select_related('home_team', 'away_team').order_by('match_date')[:5]
        ctx['my_tactics'] = Tactic.objects.filter(created_by__user=u).order_by('title')[:5]
        return ctx