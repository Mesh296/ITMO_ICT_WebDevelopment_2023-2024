# Generated by Django 4.2.7 on 2023-11-25 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tdeeapp', '0005_alter_dailydata_user_alter_userfood_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailydata',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]