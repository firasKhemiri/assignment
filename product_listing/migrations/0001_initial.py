# Generated by Django 3.0.5 on 2020-04-20 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('photo', models.CharField(blank=True, max_length=250, null=True)),
                ('school_type', models.IntegerField(choices=[(0, 'Praktijkonderwijs'), (1, 'Vmbo'), (2, 'Mbo'), (3, 'Hbo'), (4, 'Opleidingsbedrijf')])),
                ('price', models.FloatField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('end_date', models.DateTimeField()),
                ('categories', models.ManyToManyField(related_name='categories', to='product_listing.Category')),
            ],
        ),
    ]
