# Generated by Django 3.0.5 on 2020-05-11 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchaser', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='address',
            unique_together={('name',)},
        ),
    ]
