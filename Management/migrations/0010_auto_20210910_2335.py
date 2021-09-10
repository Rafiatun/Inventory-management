# Generated by Django 3.2.7 on 2021-09-10 17:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0009_alter_sale_total_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='purchase_date',
        ),
        migrations.AddField(
            model_name='sale',
            name='sale_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]