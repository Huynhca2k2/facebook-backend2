# Generated by Django 5.0.6 on 2024-05-17 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dauGiaApi', '0003_alter_interact_like_alter_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(default=None, upload_to='post/%Y/%m'),
        ),
    ]
