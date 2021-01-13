# Generated by Django 3.1.5 on 2021-01-12 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=300)),
                ('price', models.FloatField()),
                ('images', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=2500)),
                ('size', models.CharField(max_length=20)),
                ('availability', models.BooleanField()),
                ('details', models.CharField(max_length=2500)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dg.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('review', models.CharField(max_length=3000)),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dg.product')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('total', models.FloatField(null=True)),
                ('productlist', models.ManyToManyField(to='dg.Product')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
