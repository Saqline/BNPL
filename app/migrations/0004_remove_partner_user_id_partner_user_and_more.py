# Generated by Django 5.1.3 on 2024-12-08 09:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_partner_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='user_id',
        ),
        migrations.AddField(
            model_name='partner',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='partner',
            name='agreement_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='contact_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')], default='ACTIVE', max_length=50),
        ),
    ]
