from django.urls import path
from .views import (
    MatchListView, MatchCreateView,
    MatchUpdateView, MatchDeleteView, MatchDetailView
)

urlpatterns = [
    path('', MatchListView.as_view(), name='list-match'),
    path('create/', MatchCreateView.as_view(), name='create-match'),

    path('<int:pk>/', MatchDetailView.as_view(), name='details-match'),
    path('<int:pk>/edit/', MatchUpdateView.as_view(), name='edit-match'),
    path('<int:pk>/delete/', MatchDeleteView.as_view(), name='delete-match'),
]

