from django.urls import path
from .views import (
    MatchListView, MatchDetailView, MatchCreateView,
    MatchUpdateView, MatchDeleteView
)

urlpatterns = [
    path('', MatchListView.as_view(), name='list-match'),
    path('<int:pk>/', MatchDetailView.as_view(), name='details-match'),
    path('create/', MatchCreateView.as_view(), name='create-match'),
    path('<int:pk>/edit/', MatchUpdateView.as_view(), name='edit-match'),
    path('<int:pk>/delete/', MatchDeleteView.as_view(), name='delete-match'),
]

