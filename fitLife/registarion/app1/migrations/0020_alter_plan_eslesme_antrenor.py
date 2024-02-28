# Generated by Django 4.2.7 on 2023-12-05 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0019_egzersiz_beslenme_planlari_baslik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan_eslesme',
            name='antrenor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]