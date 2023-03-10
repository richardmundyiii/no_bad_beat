# Generated by Django 4.1.7 on 2023-03-08 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.CharField(max_length=100)),
                ('game_date', models.DateField(blank=True)),
                ('away_team', models.CharField(max_length=100)),
                ('home_team', models.CharField(max_length=100)),
                ('away_price', models.IntegerField()),
                ('home_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_user', models.CharField(max_length=100)),
                ('comment_date', models.DateField(blank=True)),
                ('comment', models.TextField(max_length=250)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.game')),
            ],
        ),
    ]
