# Generated by Django 3.0.5 on 2020-05-21 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200521_0204'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='profilepic',
            field=models.ImageField(default=1, upload_to='profilepic'),
            preserve_default=False,
        ),
    ]