# Generated by Django 4.0.1 on 2022-01-30 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviesbackend', '0006_alter_rating_date_alter_watchlater_dateset'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='watchlater',
            unique_together=set(),
        ),
    ]