# Generated by Django 4.0.4 on 2022-11-29 14:07

import datetime
from django.db import migrations, models
import django.db.models.deletion
import froala_editor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCatagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('bg', models.ImageField(null=True, upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='blogField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('display_img', models.ImageField(null=True, upload_to='img')),
                ('display_img_caption', models.CharField(max_length=200, null=True)),
                ('views', models.IntegerField(default=0)),
                ('discription', models.TextField(blank=True)),
                ('content', froala_editor.fields.FroalaField()),
                ('feature_article', models.BooleanField(default=False)),
                ('hidepost', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='publishingUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('img', models.ImageField(null=True, upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=200, unique=True)),
                ('image', models.ImageField(null=True, upload_to='img')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloggingPage.blogfield')),
            ],
        ),
        migrations.AddField(
            model_name='blogfield',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloggingPage.publishinguser'),
        ),
        migrations.AddField(
            model_name='blogfield',
            name='blog_catagory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloggingPage.blogcatagory'),
        ),
        migrations.AddField(
            model_name='blogfield',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloggingPage.position'),
        ),
        migrations.AddField(
            model_name='blogfield',
            name='related_blog',
            field=models.ManyToManyField(blank=True, to='bloggingPage.blogfield'),
        ),
        migrations.AddField(
            model_name='blogfield',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='bloggingPage.tags'),
        ),
    ]
