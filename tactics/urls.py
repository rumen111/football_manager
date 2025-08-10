from django.urls import path
from .views import (
    TacticListView, TacticDetailView, TacticCreateView,
    TacticUpdateView, TacticDeleteView
)

urlpatterns = [
    path('', TacticListView.as_view(), name='list-tactic'),
    path('<int:pk>/', TacticDetailView.as_view(), name='details-tactic'),
    path('create/', TacticCreateView.as_view(), name='create-tactic'),
    path('<int:pk>/edit/', TacticUpdateView.as_view(), name='edit-tactic'),
    path('<int:pk>/delete/', TacticDeleteView.as_view(), name='delete-tactic'),
]

