# Generated by Django 4.1.7 on 2023-04-04 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_rename_instrument_artist_instruments'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrument',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
