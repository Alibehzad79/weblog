# Generated by Django 4.2 on 2023-05-06 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlePageAds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('url', models.URLField(help_text='https://...', verbose_name='لینک')),
                ('file', models.FileField(help_text='نوع فایل: گیف', upload_to='files/ads/', verbose_name='فایل')),
                ('date_created', models.DateTimeField(verbose_name='تاریخ ایجاد')),
                ('expiry_date', models.DateTimeField(verbose_name='تاریخ انقضاء')),
                ('pay', models.CharField(max_length=100, verbose_name='هزینه پرداختی')),
                ('active', models.BooleanField(verbose_name='فعال')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='سازنده تبلیغ')),
            ],
            options={
                'verbose_name': 'تبلیغ',
                'verbose_name_plural': 'تبلیغات صفحه هات مقاله ها',
            },
        ),
    ]