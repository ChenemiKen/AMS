# Generated by Django 3.1.6 on 2021-07-02 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amapp', '0002_auto_20210701_0446'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='session_id',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
