# Generated by Django 4.2.6 on 2023-12-22 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestblood',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]