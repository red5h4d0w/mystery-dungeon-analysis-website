# Generated by Django 3.2.8 on 2021-10-11 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='version',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]