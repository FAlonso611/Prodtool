# Generated by Django 2.1.3 on 2019-05-10 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_add_subscription'),
        ('feedback', '0021_customerfeedbackimportersettings_feedback_tag_name'),
        ('appaccounts', '0014_auto_20190503_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterableAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('friendly_name', models.CharField(max_length=256)),
                ('related_object_type', models.CharField(choices=[('APPUSER', 'Person'), ('APPCOMPANY', 'Company')], max_length=256)),
                ('attribute_type', models.CharField(choices=[('str', 'String'), ('bool', 'True/False'), ('float', 'Float'), ('int', 'Integer')], max_length=256)),
                ('widget', models.CharField(choices=[('Select', 'Select'), ('GroupedSelect', 'Grouped Select')], max_length=256)),
                ('is_custom', models.BooleanField()),
                ('show_in_filters', models.BooleanField(default=False)),
                ('is_mrr', models.BooleanField(default=False)),
                ('is_plan', models.BooleanField(default=False)),
                ('show_in_badge', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Customer')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.FeedbackImporter')),
            ],
        ),
    ]