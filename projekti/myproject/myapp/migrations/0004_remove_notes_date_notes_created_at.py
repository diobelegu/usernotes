# Generated by Django 4.2.7 on 2024-01-17 20:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_notes_date_alter_notes_user_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='date',
        ),
        migrations.AddField(
            model_name='notes',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
