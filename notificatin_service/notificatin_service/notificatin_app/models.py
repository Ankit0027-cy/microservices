# notification_service/notification_app/models.py
from django.db import models
import uuid

class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    userId = models.UUIDField()
    message = models.TextField()
    read = models.BooleanField(default=False)

