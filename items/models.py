from django.db import models

# Create your models here.

class Item(models.Model):
	row_id = models.AutoField(primary_key=True)
	item_type = models.CharField(max_length=100)
	year = models.CharField(max_length=10)
	revenue = models.IntegerField()

	def __str__(self):
		return self.item_type + ' : ' + self.year
