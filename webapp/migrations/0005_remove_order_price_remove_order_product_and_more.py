# Generated by Django 4.2.3 on 2023-07-13 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_order_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.CreateModel(
            name='order_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0.0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.product')),
            ],
        ),
    ]