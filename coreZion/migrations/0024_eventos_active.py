# Generated by Django 3.0.6 on 2020-07-07 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreZion', '0023_eventos'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]