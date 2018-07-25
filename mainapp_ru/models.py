from django.db import models


# Create your models here.

class HomeRu(models.Model):
    name = models.CharField(max_length=30, blank=True)
    h1 = models.CharField(max_length=30, blank=True)
    paragraph1 = models.TextField(blank=True)
    paragraph2 = models.TextField(blank=True)
    paragraph3 = models.TextField(blank=True)
    paragraph4 = models.TextField(blank=True)
    paragraph5 = models.TextField(blank=True)
    paragraph6 = models.TextField(blank=True)
    paragraph7 = models.TextField(blank=True)
    paragraph8 = models.TextField(blank=True)
    paragraph9 = models.TextField(blank=True)
    paragraph10 = models.TextField(blank=True)
    paragraph11 = models.TextField(blank=True)
    paragraph12 = models.TextField(blank=True)
    paragraph13 = models.TextField(blank=True)

    class Meta():
        verbose_name_plural = "Страницы"

    def __str__(self):
        return self.name


class InnerHomeRu(models.Model):
    outer_relation = models.ForeignKey(HomeRu, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    h2 = models.CharField(max_length=30, blank=True)


    class Meta():
        verbose_name_plural = "Вложенные страницы"

    def __str__(self):
        return self.name
