# Generated by Django 2.1.2 on 2018-11-28 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginpage', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='ProfessionalBehaviour',
        ),
        migrations.DeleteModel(
            name='SecurityTraining',
        ),
    ]
