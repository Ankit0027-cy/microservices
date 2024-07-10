# notification_service/notification_app/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [
    path('api/notifications/', [
        path('', views.NotificationListView.as_view(), name='notification_list'),
        path('create/', views.CreateNotificationView.as_view(), name='create_notification'),
        path('<int:pk>/', views.NotificationDetailView.as_view(), name='notification_detail'),
    ]),
]
