# Generated by Django 3.0.8 on 2020-08-06 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_post_deneme_resim'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='deneme_resim2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='deneme_resim3',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
