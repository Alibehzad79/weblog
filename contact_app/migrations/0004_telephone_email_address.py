# Generated by Django 4.2 on 2023-04-26 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0003_alter_contactmodelform_answre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telephone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20, verbose_name='شماره تلفن')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='telephones', to='contact_app.contactmodel', verbose_name='تماس با ما')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='شماره تلفن')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='emails', to='contact_app.contactmodel', verbose_name='تماس با ما')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150, verbose_name='شماره تلفن')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='addresses', to='contact_app.contactmodel', verbose_name='تماس با ما')),
            ],
        ),
    ]