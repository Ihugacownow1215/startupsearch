# Generated by Django 4.1.4 on 2022-12-13 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Company Name')),
                ('company_linkedin_names', models.JSONField(blank=True, default=None, null=True, verbose_name='Array of company linkedin names')),
                ('headcount', models.IntegerField(blank=True, default=None, null=True, verbose_name='Number of people in company')),
                ('known_total_funding', models.IntegerField(blank=True, default=None, null=True, verbose_name='Public valuation')),
                ('investors', models.JSONField(blank=True, default=None, null=True, verbose_name='Investor List')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Name of Person')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('company_li_name', models.CharField(max_length=255, null=True)),
                ('last_title', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField(null=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mvpapp.company')),
            ],
        ),
    ]
