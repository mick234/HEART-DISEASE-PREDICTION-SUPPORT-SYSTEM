# Generated by Django 3.1.4 on 2021-04-30 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20210501_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthblog',
            name='pic',
            field=models.ImageField(blank=True, default='logo.png', null=True, upload_to='static/images'),
        ),
    ]
