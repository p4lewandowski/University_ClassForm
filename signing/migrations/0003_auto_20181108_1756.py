# Generated by Django 2.1.2 on 2018-11-08 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signing', '0002_auto_20181108_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='index',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
