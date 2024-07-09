# notification_service/notification_app/urls.py
from django.urls import path
from .views import NotificationListCreateView, NotificationDetailView

urlpatterns = [
    path('notifications/', NotificationListCreateView.as_view(), name='notifications'),
    path('notifications/<uuid:id>/', NotificationDetailView.as_view(), name='notification_detail'),
]
