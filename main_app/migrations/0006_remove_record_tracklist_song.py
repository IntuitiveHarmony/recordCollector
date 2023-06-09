# Generated by Django 4.1.7 on 2023-03-31 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_band_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='trackList',
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trackNumber', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=100)),
                ('length', models.DurationField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.record')),
            ],
        ),
    ]
