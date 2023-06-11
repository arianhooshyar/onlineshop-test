from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class Products(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    Datetime_create = models.DateTimeField(auto_now_add=True)
    Datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_Detail', args=[self.pk])


class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', 'very bad'),
        ('2', 'Bad'),
        ('3', 'Normal'),
        ('4', 'Good'),
        ('5', 'Perfect'),
    ]
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='comments', )
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments', )
    body = models.TextField(verbose_name='متن')
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS, verbose_name='امتیاز')
    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
