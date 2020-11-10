# Generated by Django 2.1.3 on 2019-09-23 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0027_add_default_sort_to_themes'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='import_token',
            field=models.CharField(blank=True, help_text='Used to keep track of all of the items created in a single admin import for easy deletion in case of disaster.', max_length=36),
        ),
        migrations.AddField(
            model_name='theme',
            name='import_token',
            field=models.CharField(blank=True, help_text='Used to keep track of all of the items created in a single admin import for easy deletion in case of disaster.', max_length=36),
        ),
    ]
