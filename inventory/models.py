from django.db import models

class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    detail = models.TextField()
    category = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    def snippet(self):
        return self.detail[:50] + '...'
