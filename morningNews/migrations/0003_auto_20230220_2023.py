# Generated by Django 3.2.9 on 2023-02-20 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morningNews', '0002_auto_20230220_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsdiscription',
            name='catagory',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsdiscription',
            name='discription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Discription',
        ),
    ]
