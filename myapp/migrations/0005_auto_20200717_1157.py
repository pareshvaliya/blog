# Generated by Django 3.0.8 on 2020-07-17 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200716_0916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Comment',
            new_name='comment',
        ),
    ]