# Generated by Django 4.1 on 2022-10-04 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faperta', '0002_alter_mahasiswa_nim_alter_mahasiswa_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dosen',
            name='foto',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='mahasiswa',
            name='foto',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='foto',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
