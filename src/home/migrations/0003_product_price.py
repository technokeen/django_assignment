# Generated by Django 3.1.7 on 2021-03-26 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
