# Generated by Django 4.2.7 on 2023-11-25 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tdeeapp', '0008_alter_dailydata_user_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfood',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]