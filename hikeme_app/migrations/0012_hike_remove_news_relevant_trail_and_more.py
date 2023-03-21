# Generated by Django 4.1.1 on 2023-03-21 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hikeme_app', '0011_remove_person_statuses_status_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='news',
            name='relevant_trail',
        ),
        migrations.RemoveField(
            model_name='news',
            name='relevant_trail_checkpoint',
        ),
        migrations.RemoveField(
            model_name='person',
            name='current_trail',
        ),
        migrations.RemoveField(
            model_name='person',
            name='current_trail_checkpoint',
        ),
        migrations.AddField(
            model_name='trail',
            name='difficulty',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trail',
            name='length',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='checkin',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hikeme_app.person'),
        ),
        migrations.DeleteModel(
            name='Leaderboard',
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.AddField(
            model_name='hike',
            name='checkins',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hikeme_app.checkin'),
        ),
        migrations.AddField(
            model_name='hike',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hikeme_app.person'),
        ),
        migrations.AddField(
            model_name='hike',
            name='trail',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hikeme_app.trail'),
        ),
    ]