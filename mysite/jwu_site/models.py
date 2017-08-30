# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class JianWu(models.Model):
    name = models.CharField(primary_key=True)
    Introduction = models.TextField(null=False)
    img = models.ImageField(null=False)


class WorkExperience(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    start = models.DateField(null=False)
    end = models.DateField()
    duty = models.TextField(null=False)


class Education(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    degree = models.TextField(null=False)
    start = models.DateField(null=False)
    end = models.DateField()
    descriptin = models.TextField(null=False)
    