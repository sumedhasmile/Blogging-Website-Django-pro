# Generated by Django 3.0.6 on 2020-09-14 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_student_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='roll_no',
            field=models.CharField(max_length=50, null=True),
        ),
    ]