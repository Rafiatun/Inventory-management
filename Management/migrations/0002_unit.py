# Generated by Django 3.2.7 on 2021-09-10 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('short_name', models.CharField(max_length=12)),
            ],
        ),
    ]
