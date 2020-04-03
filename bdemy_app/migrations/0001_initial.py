# Generated by Django 3.0.4 on 2020-04-03 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('about', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='img/tutor-img/')),
                ('linkedin', models.CharField(blank=True, max_length=100)),
                ('facebook', models.CharField(blank=True, max_length=100)),
                ('telegram', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('instructor', models.CharField(max_length=100)),
                ('duration_hour', models.CharField(blank=True, default='0', max_length=10)),
                ('duration_min', models.CharField(blank=True, default='0', max_length=10)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField(blank=True)),
                ('end_date', models.DateTimeField(blank=True)),
                ('published_date', models.DateTimeField(blank=True)),
                ('FAQs', models.TextField(blank=True)),
                ('tutor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='bdemy_app.Tutor')),
            ],
        ),
    ]
