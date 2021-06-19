# Generated by Django 3.0.6 on 2020-05-31 00:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('coreZion', '0005_auto_20200530_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faixa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cor', models.CharField(max_length=100, verbose_name='Graduação')),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data da criação')),
            ],
            options={
                'verbose_name_plural': 'faixas',
            },
        ),
        migrations.AlterModelOptions(
            name='atleta',
            options={'verbose_name_plural': 'atletas'},
        ),
        migrations.RemoveField(
            model_name='atleta',
            name='data_publicacao',
        ),
        migrations.AddField(
            model_name='atleta',
            name='nomesobre',
            field=models.CharField(default=1, max_length=100, verbose_name='Nome Copleto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='atleta',
            name='graduacao',
            field=models.CharField(max_length=50, verbose_name='Graduação'),
        ),
        migrations.AlterField(
            model_name='atleta',
            name='nome',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
    ]