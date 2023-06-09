# Generated by Django 4.0 on 2022-10-23 16:49

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import newsapp.Manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Логин')),
                ('first_name', models.CharField(db_index=True, max_length=150, verbose_name='Имя')),
                ('last_name', models.CharField(db_index=True, max_length=150, verbose_name='Фамилия')),
                ('surname', models.CharField(db_index=True, max_length=150, verbose_name='Отчество')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, verbose_name='электоронная почта')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False, verbose_name='Персонал')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
                'ordering': ['id'],
            },
            managers=[
                ('objects', newsapp.Manager.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='last_News_date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trues', models.BooleanField(default=False, verbose_name='Этот период')),
                ('last_news_date', models.DateTimeField(verbose_name='Период для недавных новостей')),
            ],
            options={
                'verbose_name': 'Последние новости',
                'verbose_name_plural': 'Последние новости',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor.fields.RichTextField(db_index=True, verbose_name='Наименования новости')),
                ('context', ckeditor.fields.RichTextField(db_index=True, verbose_name='Краткое описание новости')),
                ('image1', models.ImageField(blank=True, db_index=True, upload_to='', verbose_name='Изображения')),
                ('image2', models.ImageField(blank=True, db_index=True, null=True, upload_to='', verbose_name='Изображения')),
                ('image3', models.ImageField(blank=True, db_index=True, null=True, upload_to='', verbose_name='Изображения')),
                ('date_add', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Дата создания ленты')),
                ('content_text', ckeditor.fields.RichTextField(db_index=True, verbose_name='Текст новости')),
                ('main_news', models.BooleanField(db_index=True, default=False, verbose_name='Главные новости')),
                ('category', models.CharField(db_index=True, default='новая запись', max_length=150, verbose_name='Категория')),
                ('published', models.BooleanField(db_index=True, default=False, verbose_name='Публиковать')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsapp.author', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-id'],
            },
        ),
    ]
