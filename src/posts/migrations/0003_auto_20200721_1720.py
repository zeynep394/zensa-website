# Generated by Django 3.0.8 on 2020-07-21 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200721_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='f_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='l_price',
            field=models.FloatField(default=0),
        ),
    ]
