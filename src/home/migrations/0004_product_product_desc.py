# Generated by Django 3.1.7 on 2021-03-26 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_desc',
            field=models.CharField(default=200, max_length=300),
        ),
    ]