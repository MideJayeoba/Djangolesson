# Generated by Django 5.1.2 on 2024-11-04 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='weight',
            field=models.FloatField(null=True),
        ),
    ]
