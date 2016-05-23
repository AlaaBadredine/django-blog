from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey('auth.User')
    Trait = models.CharField(max_length=200, blank=True)
    Functional_SNPs = models.CharField(max_length=200, blank=True)
    TAG_SNPs= models.CharField(max_length=200, default="")
    Reference = models.CharField(max_length=200, blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.TAG_SNPs

