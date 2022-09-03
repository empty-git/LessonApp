# Generated by Django 4.1 on 2022-09-03 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Назва')),
                ('type_lesson', models.CharField(choices=[('Лекція', 'Лекція'), ('Практична робота', 'Практична робота'), ('Лабораторна робота', 'Лабораторна робота'), ('Тест', 'Тест')], default='Лекція', max_length=50, verbose_name='Тип заняття')),
                ('pdf_file', models.FileField(null=True, upload_to='', verbose_name='Файл')),
                ('additional_information', models.CharField(max_length=500, null=True, verbose_name='Додаткова інформація')),
            ],
        ),
    ]
