# Generated by Django 4.2.7 on 2023-12-03 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_userinformation_profilfotografi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='profilFotografi',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images'),
        ),
    ]
