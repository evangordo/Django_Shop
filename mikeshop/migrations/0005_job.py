# Generated by Django 4.1.1 on 2022-10-03 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mikeshop', '0004_remove_product_category_remove_product_test_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('avatar', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]
