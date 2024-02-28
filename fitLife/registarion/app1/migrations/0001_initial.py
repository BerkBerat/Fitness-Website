# Generated by Django 4.2.7 on 2023-12-03 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='userInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=50)),
                ('soyad', models.CharField(max_length=50)),
                ('dogumTarihi', models.DateField()),
                ('cinsiyet', models.CharField(choices=[('E', 'Erkek'), ('K', 'Kadın'), ('D', 'Diğer')], max_length=1, null=True)),
                ('telefonNumarasi', models.CharField(max_length=20)),
                ('profilFotografi', models.CharField(max_length=50)),
                ('rol', models.CharField(default='null', max_length=20)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='danisan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kilo', models.FloatField()),
                ('boy', models.FloatField()),
                ('vucutYagOrani', models.FloatField()),
                ('kasKutlesi', models.FloatField()),
                ('vucutKitleIndeksi', models.FloatField()),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.userinformation')),
            ],
        ),
        migrations.CreateModel(
            name='antrenor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uzmanlikAlani', models.CharField(choices=[('KA', 'Kilo Aldırma'), ('KV', 'Kilo Verdirme'), ('KK', 'Kilo Koruma'), ('KKA', 'Kas Kazandırma')], max_length=3, null=True)),
                ('deneyim', models.CharField(max_length=20)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]