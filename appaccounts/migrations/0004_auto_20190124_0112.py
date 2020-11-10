# Generated by Django 2.1.3 on 2019-01-24 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('appaccounts', '0003_auto_20181123_2328'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='appcompany',
            unique_together={('customer', 'remote_id')},
        ),
        migrations.AlterUniqueTogether(
            name='appuser',
            unique_together={('customer', 'remote_id'), ('customer', 'email')},
        ),
    ]
