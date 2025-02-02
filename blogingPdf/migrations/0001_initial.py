# Generated by Django 3.2.9 on 2023-01-31 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BachelorField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.CharField(max_length=200, null=True)),
                ('color', models.CharField(max_length=200, null=True)),
                ('BachelorField', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogingPdf.bachelorfield')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200, null=True)),
                ('color', models.CharField(max_length=200, null=True)),
                ('sem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogingPdf.sem')),
            ],
        ),
        migrations.CreateModel(
            name='BookPdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_name', models.FileField(null=True, upload_to='documents/')),
                ('BachelorField', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogingPdf.bachelorfield')),
                ('sem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogingPdf.sem')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogingPdf.subject')),
            ],
        ),
    ]
