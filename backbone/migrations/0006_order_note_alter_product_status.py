# Generated by Django 4.1 on 2023-04-07 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backbone', '0005_order_status_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('A', 'Available'), ('P', 'Pending'), ('S', 'Sold')], max_length=1),
        ),
    ]
