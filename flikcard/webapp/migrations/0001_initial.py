# Generated by Django 3.2.6 on 2021-10-16 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=10000, null=True)),
                ('price', models.CharField(blank=True, default=None, max_length=10000, null=True)),
                ('description', models.CharField(blank=True, default=None, max_length=10000, null=True)),
                ('category', models.CharField(blank=True, default=None, max_length=10000, null=True)),
                ('image', models.CharField(blank=True, default=None, max_length=10000, null=True)),
                ('rate', models.CharField(blank=True, default=None, max_length=10000, null=True)),
                ('count', models.CharField(blank=True, default=None, max_length=10000, null=True)),
            ],
        ),
    ]
