from django.urls import path
from .views import ServerCreateView, ServerListView, ServerStatusView, ServerIncidentsView

urlpatterns = [
    path('servers/add/', ServerCreateView.as_view(), name='server-create'),
    path('servers/', ServerListView.as_view(), name='server-list'),
    path('servers/<int:pk>/status/', ServerStatusView.as_view(), name='server-status'),
    path('servers/<int:pk>/incidents/', ServerIncidentsView.as_view(), name='server-incidents'),
]
