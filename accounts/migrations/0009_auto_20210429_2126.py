# Generated by Django 3.1.4 on 2021-04-29 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210429_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthblog',
            name='picture',
            field=models.ImageField(blank=True, default='profile1.png', null=True, upload_to=''),
        ),
    ]
