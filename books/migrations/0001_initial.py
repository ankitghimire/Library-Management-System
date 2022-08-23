# Generated by Django 4.0.1 on 2022-01-22 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('publication_name', models.CharField(blank=True, max_length=300, null=True)),
                ('publication_date', models.DateField()),
                ('author', models.ManyToManyField(to='books.Author')),
            ],
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='BookCopies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=17, unique=True)),
                ('rfid', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.bookcategory'),
        ),
    ]
