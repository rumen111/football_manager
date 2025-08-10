from django.urls import path
from .views import (
    TeamListView, TeamDetailView, TeamCreateView,
    TeamUpdateView, TeamDeleteView
)

urlpatterns = [
    path('', TeamListView.as_view(), name='list-team'),
    path('<int:pk>/', TeamDetailView.as_view(), name='details-team'),
    path('create/', TeamCreateView.as_view(), name='create-team'),
    path('<int:pk>/edit/', TeamUpdateView.as_view(), name='edit-team'),
    path('<int:pk>/delete/', TeamDeleteView.as_view(), name='delete-team'),
]