# Generated by Django 4.2.1 on 2024-01-13 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomemedico', models.CharField(max_length=250)),
                ('nomepaciente', models.CharField(max_length=250)),
                ('data', models.CharField(max_length=15)),
                ('horario', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=250)),
            ],
        ),
    ]
