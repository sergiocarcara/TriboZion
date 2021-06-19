# Generated by Django 3.0.6 on 2020-05-30 16:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atletas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('graduacao', models.CharField(max_length=100)),
                ('texto', models.TextField(max_length=500)),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data da criação')),
                ('data_publicacao', models.DateTimeField(blank=True, null=True, verbose_name='Data da publicação')),
            ],
        ),
    ]