# Generated by Django 4.1.10 on 2023-09-26 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='video_url',
            new_name='video_link',
        ),
        migrations.RenameField(
            model_name='lessonview',
            old_name='watched',
            new_name='is_watched',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='total_duration_seconds',
        ),
        migrations.RemoveField(
            model_name='lessonview',
            name='watch_time_seconds',
        ),
        migrations.AddField(
            model_name='lessonview',
            name='view_time_seconds',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='duration_seconds',
            field=models.PositiveIntegerField(),
        ),
    ]
