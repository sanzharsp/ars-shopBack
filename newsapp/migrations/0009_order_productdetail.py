# Generated by Django 4.1.7 on 2023-04-11 09:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0008_remove_order_addres_order_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='productDetail',
            field=ckeditor.fields.RichTextField(db_index=True, default=0, verbose_name='Тапсырыс туралы толығырақ'),
            preserve_default=False,
        ),
    ]
