# Generated by Django 3.0.5 on 2020-05-11 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_transaction_red_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction_green',
            name='transaction',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='transaction.Transaction'),
            preserve_default=False,
        ),
    ]
