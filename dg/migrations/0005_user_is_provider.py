# Generated by Django 4.0.5 on 2022-06-26 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dg', '0004_auto_20210418_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_Provider',
            field=models.BooleanField(default=False),
        ),
    ]
