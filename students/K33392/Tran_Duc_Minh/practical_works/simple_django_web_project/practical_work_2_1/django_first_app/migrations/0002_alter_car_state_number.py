# Generated by Django 4.2.6 on 2023-10-25 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='state_number',
            field=models.CharField(max_length=15),
        ),
    ]