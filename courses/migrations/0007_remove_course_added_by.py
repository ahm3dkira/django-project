# Generated by Django 4.0.3 on 2022-04-12 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_course_added_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='added_by',
        ),
    ]
