# Generated by Django 2.1.3 on 2020-03-19 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20200220_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='is_per_seat_plan',
            field=models.BooleanField(default=True),
        ),
    ]
