# Generated by Django 2.0.2 on 2018-02-04 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_at',
            field=models.TimeField(),
        ),
    ]
