# Generated by Django 4.0.1 on 2022-01-30 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviesbackend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='rate',
            new_name='rating',
        ),
    ]