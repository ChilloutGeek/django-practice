# Generated by Django 3.0.5 on 2020-05-21 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='email',
        ),
        migrations.RemoveField(
            model_name='account',
            name='name',
        ),
        migrations.AddField(
            model_name='account',
            name='description',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
