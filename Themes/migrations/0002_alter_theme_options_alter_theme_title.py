# Generated by Django 4.1 on 2022-09-03 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Themes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='theme',
            options={'verbose_name': 'Тема', 'verbose_name_plural': 'Теми'},
        ),
        migrations.AlterField(
            model_name='theme',
            name='title',
            field=models.CharField(blank=True, max_length=70, verbose_name='Назва'),
        ),
    ]
