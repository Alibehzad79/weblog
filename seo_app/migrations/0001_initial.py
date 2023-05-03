# Generated by Django 4.2 on 2023-05-01 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog_app', '0004_alter_articlemodel_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleListSeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.TextField(blank=True, help_text='جدا سازی با کامای انگلیسی - مثال: مقاله, مقاله۲', verbose_name='کلمات کلیدی')),
                ('description', models.CharField(help_text='حداکثر 160 کاراکتر', max_length=160, verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'صفحه لیست مقاله ها',
                'verbose_name_plural': 'صفحه لیست مقاله ها',
            },
        ),
        migrations.CreateModel(
            name='HomePageSeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.TextField(blank=True, help_text='جدا سازی با کامای انگلیسی - مثال: مقاله, مقاله۲', verbose_name='کلمات کلیدی')),
                ('description', models.CharField(help_text='حداکثر 160 کاراکتر', max_length=160, verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'صفحه ی خانه',
                'verbose_name_plural': 'صفحه ی خانه',
            },
        ),
        migrations.CreateModel(
            name='ArticlesSEO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(help_text='حداکثر 50 کاراکتر', max_length=50, verbose_name='عنوان')),
                ('keywords', models.TextField(blank=True, help_text='جدا سازی با کامای انگلیسی - مثال: مقاله, مقاله۲', verbose_name='کلمات کلیدی')),
                ('description', models.CharField(help_text='حداکثر 160 کاراکتر', max_length=160, verbose_name='توضیحات')),
                ('author_name', models.CharField(help_text='حداکثر 50 کاراکتر', max_length=50, verbose_name='نام نویسنده')),
                ('refresh', models.CharField(blank=True, help_text='الزامی نیست', max_length=150, null=True, verbose_name='Refresh')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='article_seo', to='blog_app.articlemodel', verbose_name='مقاله')),
            ],
            options={
                'verbose_name': 'سئو',
                'verbose_name_plural': 'سئوی مقاله ها',
            },
        ),
    ]
