from django.urls import path
from .views import TeamSquadView, PlayerCreateForTeamView, PlayerUpdateView, PlayerDeleteView

urlpatterns = [
    path('team/<int:team_id>/', TeamSquadView.as_view(), name='squad-team'),
    path('team/<int:team_id>/create/', PlayerCreateForTeamView.as_view(), name='create-player-for-team'),
    path('<int:pk>/edit/', PlayerUpdateView.as_view(), name='edit-player'),
    path('<int:pk>/delete/', PlayerDeleteView.as_view(), name='delete-player'),
]