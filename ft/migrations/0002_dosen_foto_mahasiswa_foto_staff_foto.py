# Generated by Django 4.1 on 2022-10-05 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ft', '0001_initial'),
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
