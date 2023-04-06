# Generated by Django 4.2 on 2023-04-03 23:44

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category_app', '0001_initial'),
        ('tag_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='160 کاراکتر', max_length=160, verbose_name='عنوان')),
                ('slug', models.SlugField(help_text='مثال: article-name', max_length=160, verbose_name='اسلاگ')),
                ('content', ckeditor.fields.RichTextField(verbose_name='محتوا')),
                ('image', models.ImageField(upload_to='images/articles/', verbose_name='تصویر')),
                ('reach_count', models.IntegerField(default=0, verbose_name='تعداد ریچ پست')),
                ('impression_count', models.IntegerField(default=0, verbose_name='تعداد ایمرشن پست')),
                ('date_created', models.DateTimeField(verbose_name='تاریخ ایجاد')),
                ('date_updated', models.DateTimeField(verbose_name='تاریخ آپدیت')),
                ('status', models.CharField(choices=[('published', 'منتشر شده'), ('unpublished', 'منتشر نشده')], default='unpublished', max_length=20, verbose_name='وضعیت')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='categories', to='category_app.category', verbose_name='دسته بندی')),
                ('tags', models.ManyToManyField(to='tag_app.tag', verbose_name='تگ ها')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقاله ها',
            },
        ),
    ]
