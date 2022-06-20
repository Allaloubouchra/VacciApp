# Generated by Django 4.0.2 on 2022-06-20 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centreapp', '0005_alter_survey_blood_pressure_alter_survey_heart_rate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='blood_pressure',
            field=models.CharField(blank=True, choices=[('H', 'Hypertension'), ('N', 'Normal'), ('O', 'Hypotension')], max_length=2, null=True),
        ),
    ]