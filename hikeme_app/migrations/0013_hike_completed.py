# Generated by Django 4.1.1 on 2023-03-21 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hikeme_app', '0012_hike_remove_news_relevant_trail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hike',
            name='completed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
