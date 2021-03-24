from django.db import models

# Create your models here.


class Tool(models.Model):

    name = models.CharField(max_length=250, null=False, blank=False, verbose_name='Item')
    surname = models.CharField(max_length=250, null=False, blank=False, verbose_name='Item')

    def __str__(self):
        return self.name


class ExportSetType(models.Model):

    name = models.CharField(max_length=250, null=False, blank=False, verbose_name='name')

    def __str__(self):
        return self.name
