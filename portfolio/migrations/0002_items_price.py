# Generated by Django 3.0.8 on 2020-07-09 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
