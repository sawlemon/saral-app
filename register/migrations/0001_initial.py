# Generated by Django 3.0.3 on 2020-02-24 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=30)),
                ('college_name', models.CharField(max_length=50)),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('reg_id', models.CharField(max_length=16, unique=True)),
            ],
        ),
    ]
