# Generated by Django 2.1.5 on 2019-02-02 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_setting_allow_parallel_tracking'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='identifier',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]