# Generated by Django 5.1.1 on 2024-10-19 10:20

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ORM', '0004_alter_category_uid_alter_product_uid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('0b4fafc2-09e0-416b-8e80-d9354e23424d'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('0b4fafc2-09e0-416b-8e80-d9354e23424d'), editable=False, primary_key=True, serialize=False),
        ),
    ]
