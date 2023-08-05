# Generated by Django 4.2.4 on 2023-08-04 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('Sold', 'Sold'), ('Reserved', 'Reserved')], default='Available', max_length=10),
        ),
    ]