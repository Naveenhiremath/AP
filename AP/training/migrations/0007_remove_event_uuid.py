# Generated by Django 2.1.5 on 2019-01-11 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0006_auto_20190111_2337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='uuid',
        ),
    ]
