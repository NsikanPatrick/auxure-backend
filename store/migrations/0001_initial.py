# Generated by Django 4.2.2 on 2023-08-26 13:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('category_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('slug', models.SlugField(default=None)),
                ('icon', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('B', 'Both')], default='B', max_length=1)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Perfume',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('discount', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='img/store')),
                ('price', models.FloatField(default=100.0)),
                ('slug', models.SlugField(blank=True, default=None, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('inventory', models.IntegerField(default=5)),
                ('top_deal', models.BooleanField(default=False)),
                ('flash_sales', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='store.category')),
            ],
            options={
                'ordering': ['price'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(default='description')),
                ('customer_name', models.CharField(max_length=50)),
                ('perfume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='store.perfume')),
            ],
        ),
        migrations.CreateModel(
            name='PerfumeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='img/store')),
                ('perfume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='store.perfume')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='featured_product',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='featured_product', to='store.perfume'),
        ),
        migrations.CreateModel(
            name='Cartitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='store.cart')),
                ('perfume', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cartitems', to='store.perfume')),
            ],
        ),
    ]
