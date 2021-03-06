# Generated by Django 3.2.7 on 2021-09-10 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0005_sale'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_quantity', models.FloatField(default=0)),
                ('sale_quantity', models.FloatField(default=0)),
                ('total_balanced_quantity', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Management.product')),
                ('purchase', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Management.purchase')),
                ('sale', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Management.sale')),
            ],
        ),
    ]
