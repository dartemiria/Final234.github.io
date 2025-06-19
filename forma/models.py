from django.db import models

class Articles(models.Model):
    title = models.CharField("Название ОП")
    whatwilllearn = models.TextField("Что буду изучать")
    whatlearn = models.TextField("Чему научусь")
    pros = models.TextField("Преимущества программы")
    future = models.TextField("Перспективы после")

    def __str__(self): 
        return self.title

    class Meta:
        verbose_name = 'Другие образовательные программы' 



