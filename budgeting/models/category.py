from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    budget = models.ForeignKey('Budget', related_name='categories', on_delete=models.CASCADE)

    class Meta:
        db_table = 'CATEGORY'
    
    def __str__(self):
        return self.name