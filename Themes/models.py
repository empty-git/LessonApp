from django.db import models


# Create your models here.

class Theme(models.Model):
    LESSONS_TYPES = [
        ('Лекція', 'Лекція'),
        ('Практична робота', 'Практична робота'),
        ('Лабораторна робота', 'Лабораторна робота'),
        ('Тест', 'Тест'),
    ]
    title = models.CharField(max_length=70, verbose_name='Назва', blank=True)
    type_lesson = models.CharField(max_length=50, choices=LESSONS_TYPES,default='Лекція', verbose_name='Тип заняття')
    pdf_file = models.FileField(null=True, verbose_name='Файл', blank=True,  upload_to="pdfs")
    additional_information = models.CharField(max_length=500, null=True, verbose_name='Додаткова інформація', blank=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Теми'


