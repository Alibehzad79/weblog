# Generated by Django 4.2 on 2023-04-06 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0002_alter_contactmodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodelform',
            name='answre',
            field=models.TextField(blank=True, null=True, verbose_name='جواب'),
        ),
    ]
