# Generated by Django 3.2.9 on 2023-02-20 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morningNews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discription',
            name='publish',
        ),
        migrations.AlterField(
            model_name='discription',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]