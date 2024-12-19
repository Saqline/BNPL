# Generated by Django 5.1.3 on 2024-12-09 09:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_partner_user_id_partner_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.RenameField(
            model_name='apikey',
            old_name='key_name',
            new_name='encoded_key',
        ),
        migrations.RenameField(
            model_name='installment',
            old_name='late_pay_alert_sent',
            new_name='installment_alert_sent_count',
        ),
        migrations.RenameField(
            model_name='latepayment',
            old_name='amount_due',
            new_name='due_amount_with_penalty',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='created_at',
            new_name='payment_date',
        ),
        migrations.RenameField(
            model_name='plan',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='plan',
            old_name='commission_rate',
            new_name='partner_commission_rate',
        ),
        migrations.RenameField(
            model_name='plan',
            old_name='fixed_rate',
            new_name='system_commission_rate',
        ),
        migrations.RenameField(
            model_name='plan',
            old_name='update_date',
            new_name='update_at',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='created_date_time',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='per_installment_amount',
            new_name='customer_per_installment_amount',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='is_balance_update',
            new_name='is_Create_by_Partner',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='partner_id',
            new_name='total_installment',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='update_date',
            new_name='updated_at',
        ),
        migrations.RemoveField(
            model_name='apikey',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='balance',
            name='partner_id',
        ),
        migrations.RemoveField(
            model_name='bank',
            name='partner_id',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='partner_id',
        ),
        migrations.RemoveField(
            model_name='installment',
            name='pay_link_alert_sent',
        ),
        migrations.RemoveField(
            model_name='latepayment',
            name='payment_date',
        ),
        migrations.RemoveField(
            model_name='latepayment',
            name='status',
        ),
        migrations.RemoveField(
            model_name='latepayment',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='count',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='expiration_date',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='is_enabled',
        ),
        migrations.RemoveField(
            model_name='refund',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='report',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='report',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='created_by',
        ),
        migrations.AddField(
            model_name='apikey',
            name='name',
            field=models.CharField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apikey',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='balance',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bank',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='create_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_create_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customer',
            name='updated_by',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='installment',
            name='is_pay_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='installment',
            name='payment_link',
            field=models.URLField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='installment',
            name='product_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='installment',
            name='status_commnents',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='latepayment',
            name='partner_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='latepayment',
            name='product_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='product_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plan',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='create_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='refund',
            name='product_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settlement',
            name='status_commnents',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='create_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='is_settlement_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='transaction',
            name='status_commnents',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='installment',
            name='partner_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='installment',
            name='transaction_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.transaction'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='installment_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.installment'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='partner_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='payment',
            name='transaction_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.transaction'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_plans', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='plan',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_plans', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='refund',
            name='partner_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='report',
            name='generated_by',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='settlement',
            name='partner_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='settlement',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed'), ('REFUND', 'Refund'), ('OTHERS', 'Others')], max_length=50),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='settlement_id',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed'), ('REFUND', 'Refund'), ('OTHERS', 'Others')], max_length=50),
        ),
    ]