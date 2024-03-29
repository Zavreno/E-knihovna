# Generated by Django 5.0.1 on 2024-02-01 15:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='up_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date uploaded'),
        ),
        migrations.AddField(
            model_name='book',
            name='web_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
