from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=50, unique= True)
    edition = models.CharField(max_length=200)
    price = models.FloatField()
    record_date = models.DateTimeField(auto_now_add= True,)
    update_date = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.title