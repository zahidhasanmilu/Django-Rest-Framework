from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    father_name = models.CharField(max_length=50)
    gender = models.ForeignKey(
        'Gender', on_delete=models.CASCADE, blank=True, null=True)
    slug = AutoSlugField(populate_from='name', unique=True, blank=True,)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home", kwargs={"slug": self.name})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Gender(models.Model):
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.gender
