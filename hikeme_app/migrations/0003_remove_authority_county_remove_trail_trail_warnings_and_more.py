# Generated by Django 4.0.6 on 2022-07-31 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hikeme_app', '0002_authority_person_status_trail_delete_login_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authority',
            name='county',
        ),
        migrations.RemoveField(
            model_name='trail',
            name='trail_warnings',
        ),
        migrations.CreateModel(
            name='Warning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warning', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField()),
                ('trail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hikeme_app.trail')),
            ],
        ),
    ]