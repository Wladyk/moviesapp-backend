# Generated by Django 4.0.1 on 2022-01-30 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesbackend', '0005_alter_movie_releasedate_alter_rating_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='watchlater',
            name='dateSet',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
