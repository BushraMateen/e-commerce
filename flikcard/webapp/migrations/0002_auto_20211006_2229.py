# Generated by Django 3.2.6 on 2021-10-06 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='discounted_price',
            field=models.CharField(blank=True, default=None, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.CharField(blank=True, default=None, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_name',
            field=models.CharField(blank=True, default=None, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='retail_price',
            field=models.CharField(blank=True, default=None, max_length=10000, null=True),
        ),
    ]