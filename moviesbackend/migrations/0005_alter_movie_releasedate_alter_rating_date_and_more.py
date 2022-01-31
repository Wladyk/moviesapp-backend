# Generated by Django 4.0.1 on 2022-01-30 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesbackend', '0004_remove_movie_totalrating_alter_rating_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='releaseDate',
            field=models.DateField(default='2022-01-30'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='date',
            field=models.DateTimeField(default='2022-01-30 20:36:28'),
        ),
        migrations.AlterField(
            model_name='watchlater',
            name='dateSet',
            field=models.DateTimeField(default='2022-01-30 20:36:28'),
        ),
        migrations.AlterUniqueTogether(
            name='watchlater',
            unique_together={('user', 'movie')},
        ),
    ]