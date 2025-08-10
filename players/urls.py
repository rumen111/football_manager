from django.urls import path
from .views import (
    PlayerListView, PlayerDetailView, PlayerCreateView,
    PlayerUpdateView, PlayerDeleteView
)

urlpatterns = [
    path('', PlayerListView.as_view(), name='list-player'),
    path('<int:pk>/', PlayerDetailView.as_view(), name='details-player'),
    path('create/', PlayerCreateView.as_view(), name='create-player'),
    path('<int:pk>/edit/', PlayerUpdateView.as_view(), name='edit-player'),
    path('<int:pk>/delete/', PlayerDeleteView.as_view(), name='delete-player'),
]

