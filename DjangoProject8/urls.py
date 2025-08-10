
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from DjangoProject8.views import IndexView, DashboardView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),

    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('accounts/', include('accounts.urls')),
    path('players/', include('players.urls')),
    path('teams/', include('teams.urls')),

    path('matches/', include('matches.urls')),
    path('tactics/', include('tactics.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)