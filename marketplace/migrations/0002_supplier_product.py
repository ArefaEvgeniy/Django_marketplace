# Generated by Django 5.1.6 on 2025-02-09 13:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('contact_email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('article', models.CharField(db_index=True, help_text='Unique string product id', max_length=100, unique=True)),
                ('available', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='marketplace.category')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='marketplace.supplier')),
            ],
            options={
                'ordering': ('category', 'quantity'),
            },
        ),
    ]
