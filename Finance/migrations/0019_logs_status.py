# Generated by Django 2.1 on 2019-03-03 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0018_logs'),
    ]

    operations = [
        migrations.AddField(
            model_name='logs',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]