# Generated by Django 3.2.20 on 2023-07-31 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tobar', '0003_auto_20230730_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cures',
            field=models.CharField(blank=True, default='autofilled on save', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.CharField(blank=True, default='autofilled on save', max_length=100),
        ),
    ]