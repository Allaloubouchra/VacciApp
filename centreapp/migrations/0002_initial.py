# Generated by Django 4.0.2 on 2022-04-17 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('centreapp', '0001_initial'),
        ('patientapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='patientapp.account')),
                ('speciality', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('time_between_dose', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VaccineCentre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField(max_length=1000)),
                ('num_phone', models.CharField(max_length=14)),
                ('latitude', models.DecimalField(decimal_places=10, max_digits=20)),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=20)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='centres', to='centreapp.city')),
            ],
        ),
        migrations.CreateModel(
            name='Wilaya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('matricule', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VaccineAndCentre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField(default=True)),
                ('centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccines', to='centreapp.vaccinecentre')),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='centres', to='centreapp.vaccine')),
            ],
        ),
        migrations.AddField(
            model_name='vaccine',
            name='vaccine_centre',
            field=models.ManyToManyField(through='centreapp.VaccineAndCentre', to='centreapp.VaccineCentre'),
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('vaccination_appointment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='patientapp.vaccinationappointment')),
                ('positive_covid', models.BooleanField(default=False)),
                ('contamination', models.BooleanField(default=False)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('heart_rate', models.PositiveIntegerField()),
                ('respiratory_rate', models.PositiveIntegerField()),
                ('blood_pressure', models.DecimalField(decimal_places=2, max_digits=5)),
                ('oximetry', models.DecimalField(decimal_places=2, max_digits=5)),
                ('disease', models.ManyToManyField(blank=True, to='centreapp.Disease')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='wilaya',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='centreapp.wilaya'),
        ),
        migrations.CreateModel(
            name='WorkingHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.PositiveIntegerField(choices=[(1, 'Saturday'), (2, 'Sunday'), (3, 'Monday'), (4, 'Thursday'), (5, 'Wednesday'), (6, 'Thursday'), (7, 'Friday')], verbose_name='day of week')),
                ('from_hour', models.TimeField(blank=True, null=True, verbose_name='from hour')),
                ('to_hour', models.TimeField(blank=True, null=True, verbose_name='to hour')),
                ('from_hour_s', models.TimeField(blank=True, null=True, verbose_name='from hour')),
                ('to_hour_s', models.TimeField(blank=True, null=True, verbose_name='to hour')),
                ('centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centreapp.vaccinecentre')),
            ],
            options={
                'unique_together': {('centre', 'day_of_week')},
            },
        ),
    ]
