# Generated by Django 3.1.8 on 2022-03-22 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(blank=True, max_length=50, null=True)),
                ('customer', models.CharField(blank=True, max_length=50, null=True)),
                ('shipping_status', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
