# Generated by Django 3.0.6 on 2020-09-14 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='branch',
            field=models.CharField(default='CS', max_length=50),
        ),
    ]
