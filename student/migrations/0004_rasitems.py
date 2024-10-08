# Generated by Django 5.0.7 on 2024-08-12 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_naturalsitems'),
    ]

    operations = [
        migrations.CreateModel(
            name='RaSitems',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('price', models.IntegerField()),
                ('flag', models.CharField(max_length=1)),
                ('img', models.URLField(blank=True, max_length=1000)),
            ],
            options={
                'db_table': 'ras_items',
            },
        ),
    ]
