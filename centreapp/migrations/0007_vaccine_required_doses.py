# Generated by Django 4.0.2 on 2022-06-28 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centreapp', '0006_alter_survey_blood_pressure'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccine',
            name='required_doses',
            field=models.PositiveIntegerField(default=2),
        ),
    ]
