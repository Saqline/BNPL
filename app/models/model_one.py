from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(AbstractUser):
    roles = models.JSONField(default=list)  
    email_verified = models.BooleanField(default=False)
    ev_code = models.CharField(max_length=6, null=True, blank=True)
    ev_code_expire = models.DateTimeField(null=True, blank=True)
    fp_code = models.CharField(max_length=6, null=True, blank=True)
    fp_code_expire = models.DateTimeField(null=True, blank=True)
    
@receiver(post_save, sender=CustomUser)
def create_partner(sender, instance, created, **kwargs):
    if created and 'partner' in instance.roles:
        Partner.objects.create(user=instance)
        Balance.objects.create(user=instance, current_balance=0.0)
class Partner(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    contact_info = models.TextField(null=True, blank=True)
    agreement_details = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')], default='ACTIVE')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class Balance(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    current_balance = models.FloatField()
    last_updated = models.DateTimeField(default=timezone.now)

class ApiKey(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    encoded_key = models.CharField(max_length=255, unique=True)
    expires_at = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[('ACTIVE', 'Active'), ('REVOKED', 'Revoked')])
    created_at = models.DateTimeField(default=timezone.now)

class Bank(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    branch_name = models.CharField(max_length=255)
    swift_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class Plan(models.Model):
    id = models.AutoField(primary_key=True)
    plan_name = models.CharField(max_length=255)
    number_of_installments = models.IntegerField()
    terms = models.TextField()
    description = models.TextField()
    late_pay_upto_in_days = models.IntegerField()
    is_active = models.BooleanField(default=True)
    partner_commission_rate = models.DecimalField(max_digits=10, decimal_places=2)
    system_commission_rate = models.DecimalField(max_digits=10, decimal_places=2)
    bank_charge_amount = models.DecimalField(max_digits=10, decimal_places=2)
    auto_settle_days = models.IntegerField()
    min_settle_days = models.IntegerField()
    late_payment_fee = models.DecimalField(max_digits=10, decimal_places=2)
    highest_purchase_amount = models.DecimalField(max_digits=10, decimal_places=2)
    refund_deduct_rate = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_plans')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='updated_plans', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')])
    create_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='customer_create_by', null=True)
    updated_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)






# class Feedback(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     customer_id = models.BigIntegerField()
#     partner_id = models.BigIntegerField(blank=True, null=True)
#     message = models.TextField()
#     rating = models.IntegerField()
#     feedback_date = models.DateTimeField(default=timezone.now)
#     status = models.CharField(max_length=50, choices=[('VISIBLE', 'Visible'), ('HIDDEN', 'Hidden')])
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(auto_now=True)
