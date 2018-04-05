# Generated by Django 2.0.2 on 2018-04-05 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantsDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('address_line1', models.CharField(max_length=150)),
                ('address_line2', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=255)),
                ('applied_position', models.CharField(max_length=50)),
                ('terms_and_conditions', models.BooleanField(default=False)),
            ],
        ),
    ]