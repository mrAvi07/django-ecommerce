# Generated by Django 3.2 on 2023-12-16 16:19

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
