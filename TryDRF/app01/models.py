from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=32,  unique=True)
    address = models.CharField(max_length=128)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'publisher'
        verbose_name_plural = verbose_name


class Books(models.Model):
    title = models.CharField(max_length=20)
    publisher = models.ForeignKey('Publisher')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'books'
        verbose_name_plural = verbose_name