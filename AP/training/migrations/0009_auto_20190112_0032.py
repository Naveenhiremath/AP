# Generated by Django 2.1.5 on 2019-01-11 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0008_auto_20190112_0031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='expense_timestamp',
            new_name='event_timestamp',
        ),
    ]
