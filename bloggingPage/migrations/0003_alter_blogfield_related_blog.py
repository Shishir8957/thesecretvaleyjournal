# Generated by Django 4.0.4 on 2022-10-11 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloggingPage', '0002_alter_blogfield_related_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogfield',
            name='related_blog',
            field=models.ManyToManyField(blank=True, to='bloggingPage.blogfield'),
        ),
    ]
