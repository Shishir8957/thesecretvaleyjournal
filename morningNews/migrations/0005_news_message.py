# Generated by Django 3.2.9 on 2023-02-21 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morningNews', '0004_alter_newsdiscription_catagory'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
