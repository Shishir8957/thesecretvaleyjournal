# Generated by Django 5.0.3 on 2024-03-06 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloggingPage', '0005_alter_blogfield_related_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogfield',
            name='related_blog',
            field=models.ManyToManyField(blank=True, to='bloggingPage.blogfield'),
        ),
    ]