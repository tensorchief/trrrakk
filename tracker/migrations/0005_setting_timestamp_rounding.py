# Generated by Django 2.1.5 on 2019-02-03 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_project_identifier'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='timestamp_rounding',
            field=models.PositiveSmallIntegerField(choices=[(1, 'No rounding'), (5, '5 minutes'), (10, '10 minutes'), (15, '15 minutes'), (30, '30 minutes')], default=1),
        ),
    ]
