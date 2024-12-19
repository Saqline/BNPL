from django.db import models
from django.utils import timezone



class Notifications(models.Model):
    id = models.BigAutoField(primary_key=True)
    sender_id = models.CharField(max_length=100)
    recipient_id = models.BigIntegerField()
    notification_date = models.DateTimeField(default=timezone.now)
    read_status = models.BooleanField(default=False)
    channel = models.CharField(max_length=50, choices=[('EMAIL', 'Email'), ('SMS', 'SMS')])  # Modify as per your enums
    subject = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=50, blank=True, null=True)
    sent_date_time = models.DateTimeField()
    notification_type = models.CharField(max_length=50, choices=[('TYPE1', 'Type1'), ('TYPE2', 'Type2')])  # Modify as per your enums
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)








class Message(models.Model):
    id = models.BigAutoField(primary_key=True)
    sender_id = models.BigIntegerField()
    recipient_id = models.BigIntegerField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
    read_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class AccessPermission(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    permission_type = models.CharField(max_length=100)  # E.g., 'READ', 'WRITE', 'DELETE'
    resource = models.CharField(max_length=100)  # E.g., 'Transaction', 'Report'
    granted_at = models.DateTimeField(default=timezone.now)
    revoked_at = models.DateTimeField(blank=True, null=True)
