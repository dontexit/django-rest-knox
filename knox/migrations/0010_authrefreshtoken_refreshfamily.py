# Generated by Django 5.0.1 on 2024-01-17 05:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("knox", "0009_extend_authtoken_field"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AuthRefreshToken",
            fields=[
                (
                    "digest",
                    models.CharField(max_length=128, primary_key=True, serialize=False),
                ),
                ("token_key", models.CharField(db_index=True, max_length=25)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("expiry", models.DateTimeField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="refresh_token_set",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "swappable": "KNOX_REFRESH_TOKEN_MODEL",
            },
        ),
        migrations.CreateModel(
            name="RefreshFamily",
            fields=[
                ("parent", models.CharField(db_index=True, max_length=15)),
                ("token", models.CharField(db_index=True, max_length=15)),
                (
                    "refresh_token",
                    models.CharField(
                        db_index=True, max_length=15, primary_key=True, serialize=False
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="refresh_family_set",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "swappable": "KNOX_REFRESH_FAMILY_MODEL",
            },
        ),
    ]
