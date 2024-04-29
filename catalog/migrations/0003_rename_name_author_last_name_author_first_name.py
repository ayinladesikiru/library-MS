# Generated by Django 5.0.4 on 2024-04-16 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='name',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='author',
            name='first_name',
            field=models.CharField(blank=True, default='', help_text='Enter your name', max_length=255, null=True),
        ),
    ]
