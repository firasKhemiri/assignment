# Generated by Django 3.0.5 on 2020-04-21 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_listing', '0004_remove_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default=12, max_length=50),
            preserve_default=False,
        ),
    ]
