# Generated by Django 3.2 on 2021-04-11 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dg', '0002_category_order_product_productreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat_id', to='dg.category'),
        ),
    ]