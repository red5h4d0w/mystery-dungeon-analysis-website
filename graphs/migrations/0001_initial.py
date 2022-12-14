# Generated by Django 3.2.8 on 2021-10-11 18:22

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
                ('ascension_level', models.IntegerField(max_length=20)),
                ('max_floor', models.IntegerField(max_length=100)),
                ('win', models.BooleanField(default=False)),
                ('elapsed_time', models.FloatField()),
                ('score', models.IntegerField()),
                ('seed', models.CharField(max_length=20)),
                ('pokemon1', models.CharField(max_length=20)),
                ('pokemon2', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Relic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graphs.game')),
            ],
        ),
        migrations.CreateModel(
            name='CardChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('upgrade', models.IntegerField(default=0)),
                ('chosen', models.BooleanField(default=False)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graphs.game')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('upgrade', models.IntegerField(default=0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graphs.game')),
            ],
        ),
    ]
