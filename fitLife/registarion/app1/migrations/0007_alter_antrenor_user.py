# Generated by Django 4.2.7 on 2023-12-03 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_danisan_istek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antrenor',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.userinformation'),
        ),
    ]
