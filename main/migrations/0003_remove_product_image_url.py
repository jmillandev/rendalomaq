# Generated by Django 4.1.3 on 2022-11-18 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
    ]