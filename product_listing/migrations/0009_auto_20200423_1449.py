# Generated by Django 3.0.5 on 2020-04-23 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_listing', '0008_auto_20200423_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='school_type',
            field=models.CharField(choices=[('praktijkonderwijs', 'Praktijkonderwijs'), ('vmbo', 'Vmbo'), ('mbo', 'Mbo'), ('hbo', 'Hbo'), ('opleidingsbedrijf', 'Opleidingsbedrijf')], max_length=200),
        ),
    ]
