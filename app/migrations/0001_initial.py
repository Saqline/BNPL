# Generated by Django 5.1.3 on 2024-12-04 10:38

import django.contrib.auth.models
import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessPermission',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_id', models.BigIntegerField()),
                ('permission_type', models.CharField(max_length=100)),
                ('resource', models.CharField(max_length=100)),
                ('granted_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('revoked_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ApiKey',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('key_name', models.CharField(max_length=255, unique=True)),
                ('user_id', models.BigIntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('expires_at', models.DateTimeField()),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('REVOKED', 'Revoked')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('partner_id', models.BigIntegerField()),
                ('current_balance', models.FloatField()),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('partner_id', models.BigIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('branch_name', models.CharField(max_length=255)),
                ('swift_code', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('partner_id', models.BigIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')], max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('customer_id', models.BigIntegerField()),
                ('partner_id', models.BigIntegerField(blank=True, null=True)),
                ('message', models.TextField()),
                ('rating', models.IntegerField()),
                ('feedback_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('VISIBLE', 'Visible'), ('HIDDEN', 'Hidden')], max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Installment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('transaction_id', models.BigIntegerField()),
                ('partner_id', models.BigIntegerField()),
                ('customer_id', models.BigIntegerField()),
                ('plan_id', models.BigIntegerField()),
                ('payment_method', models.CharField(blank=True, max_length=50, null=True)),
                ('amount', models.FloatField()),
                ('due_date', models.DateTimeField()),
                ('payment_date', models.DateTimeField(blank=True, null=True)),
                ('is_late', models.BooleanField(default=False)),
                ('late_count', models.IntegerField(default=0)),
                ('pay_link_alert_sent', models.IntegerField(default=0)),
                ('late_pay_alert_sent', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('PAID', 'Paid'), ('PENDING', 'Pending'), ('OVERDUE', 'Overdue')], max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LatePayment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('customer_id', models.BigIntegerField()),
                ('amount_due', models.FloatField()),
                ('due_date', models.DateTimeField()),
                ('payment_date', models.DateTimeField(blank=True, null=True)),
                ('penalty_fee', models.FloatField()),
                ('status', models.CharField(choices=[('PAID', 'Paid'), ('UNPAID', 'Unpaid')], max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('sender_id', models.BigIntegerField()),
                ('recipient_id', models.BigIntegerField()),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('sent_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('read_status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('sender_id', models.CharField(max_length=100)),
                ('recipient_id', models.BigIntegerField()),
                ('notification_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('read_status', models.BooleanField(default=False)),
                ('channel', models.CharField(choices=[('EMAIL', 'Email'), ('SMS', 'SMS')], max_length=50)),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('sent_date_time', models.DateTimeField()),
                ('notification_type', models.CharField(choices=[('TYPE1', 'Type1'), ('TYPE2', 'Type2')], max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('contact_info', models.TextField()),
                ('agreement_details', models.TextField()),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')], max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('customer_id', models.BigIntegerField()),
                ('partner_id', models.BigIntegerField()),
                ('installment_id', models.BigIntegerField()),
                ('transaction_id', models.BigIntegerField()),
                ('amount', models.FloatField()),
                ('currency', models.CharField(max_length=10)),
                ('expiration_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('EXPIRED', 'Expired')], max_length=50)),
                ('payment_link', models.URLField(max_length=500)),
                ('count', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('plan_name', models.CharField(max_length=255)),
                ('number_of_installments', models.IntegerField()),
                ('is_enabled', models.BooleanField()),
                ('created_by', models.CharField(max_length=255)),
                ('updated_by', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('terms', models.TextField()),
                ('late_pay_upto_in_days', models.IntegerField()),
                ('description', models.TextField()),
                ('commission_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fixed_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('auto_settle_days', models.IntegerField()),
                ('min_settle_days', models.IntegerField()),
                ('bank_charge_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('late_payment_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('highest_purchase_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('refund_deduct_rate', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('currency', models.CharField(max_length=10)),
                ('status', models.CharField(choices=[('AVAILABLE', 'Available'), ('OUT_OF_STOCK', 'Out of Stock')], max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('customer_id', models.BigIntegerField()),
                ('partner_id', models.BigIntegerField()),
                ('order_id', models.BigIntegerField()),
                ('amount', models.FloatField()),
                ('currency', models.CharField(max_length=10)),
                ('refund_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('reason', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('APPROVED', 'Approved'), ('REJECTED', 'Rejected'), ('PENDING', 'Pending')], max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('report_type', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('generated_by', models.BigIntegerField()),
                ('generated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('data', models.JSONField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Settlement',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('partner_id', models.BigIntegerField()),
                ('customer_id', models.BigIntegerField()),
                ('transaction_id', models.BigIntegerField()),
                ('bank_id', models.BigIntegerField()),
                ('amount', models.FloatField()),
                ('currency', models.CharField(max_length=10)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed')], max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('settlement_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_id', models.BigIntegerField()),
                ('partner_id', models.BigIntegerField()),
                ('product_id', models.BigIntegerField()),
                ('plan_id', models.IntegerField()),
                ('settlement_id', models.BigIntegerField()),
                ('full_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(max_length=255)),
                ('payment_links', models.TextField()),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('created_date_time', models.DateTimeField(auto_now_add=True)),
                ('is_late', models.BooleanField(default=False)),
                ('payment_method', models.CharField(max_length=255)),
                ('is_flag', models.BooleanField(default=False)),
                ('merchant_earn_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bank_charge_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('system_profit_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('per_installment_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('balance_after_trans', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_first_pay_done', models.BooleanField(default=False)),
                ('created_by', models.CharField(max_length=255)),
                ('updated_by', models.CharField(max_length=255)),
                ('comments', models.TextField()),
                ('is_balance_update', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]