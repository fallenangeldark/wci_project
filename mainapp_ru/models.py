from django.db import models


# Create your models here.

class HomeRu(models.Model):
    h1 = models.CharField(max_length=30)
    paragraph1 = models.TextField(default='test1')
    paragraph2 = models.TextField(default='test2')
    paragraph3 = models.TextField(default='test3')
    paragraph4 = models.TextField(default='test4')

    class Meta():
        verbose_name_plural = "Home_page_ru"

    def __str__(self):
        return 'home_ru'
