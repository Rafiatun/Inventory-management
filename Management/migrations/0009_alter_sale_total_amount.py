# Generated by Django 3.2.7 on 2021-09-10 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0008_auto_20210910_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='total_amount',
            field=models.FloatField(editable=False),
        ),
    ]