# Generated by Django 4.0.4 on 2022-12-05 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloggingPage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogfield',
            name='views',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
