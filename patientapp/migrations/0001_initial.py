# Generated by Django 4.0.2 on 2022-04-05 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, unique=True)),
                ('last_name', models.CharField(max_length=50, unique=True)),
                ('birthday', models.DateField()),
                ('phone_num', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='VaccinationAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_appointment', models.DateField()),
                ('time_appointment', models.TimeField()),
                ('num_dose', models.IntegerField()),
                ('arm', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='patientapp.account')),
                ('vaccination_appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientapp.vaccinationappointment')),
            ],
        ),
    ]
