# Generated by Django 5.0.6 on 2024-05-17 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dauGiaApi', '0002_post_user_interact_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interact',
            name='like',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(upload_to='post/%Y/%m'),
        ),
    ]
