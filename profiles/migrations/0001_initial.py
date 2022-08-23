# Generated by Django 4.0.1 on 2022-02-13 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(upload_to='')),
                ('full_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=10, unique=True)),
                ('dob', models.DateField(verbose_name='Date Of Birth')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Rather Not Say')], max_length=1)),
                ('rfid', models.CharField(max_length=50, unique=True)),
                ('student_id', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]