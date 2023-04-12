# Generated by Django 4.1.7 on 2023-04-11 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0004_category_alter_news_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Өнім саны')),
                ('addres', models.CharField(default='ASTANA', max_length=250, verbose_name='Адресс')),
                ('post_index', models.IntegerField(verbose_name='пошта индексі')),
                ('telephone', models.CharField(max_length=250, verbose_name='телефон нөмірі')),
                ('ordered', models.BooleanField(default='Тапсырыс қабылданды')),
                ('ver_order', models.BooleanField(default='Тапсырыс орындалды')),
                ('products', models.ManyToManyField(blank=True, related_name='products', to='newsapp.news', verbose_name='Өнімдер')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Қолданушы')),
            ],
            options={
                'verbose_name': 'тапсырыс',
                'verbose_name_plural': 'Тапсырыстар',
                'ordering': ['id'],
            },
        ),
    ]