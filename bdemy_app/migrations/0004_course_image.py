# Generated by Django 3.0.4 on 2020-04-03 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdemy_app', '0003_course_enroll'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, default='img/course-img/default.jpg', upload_to='img/course-img'),
        ),
    ]
