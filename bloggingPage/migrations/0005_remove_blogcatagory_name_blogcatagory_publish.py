# Generated by Django 4.0.4 on 2022-11-29 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloggingPage', '0004_rename_hidepost_blogfield_publish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcatagory',
            name='name',
        ),
        migrations.AddField(
            model_name='blogcatagory',
            name='publish',
            field=models.BooleanField(default=False),
        ),
    ]
