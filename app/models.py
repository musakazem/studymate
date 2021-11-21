from django.db import models

# Create your models here.


class Goals(models.Model):

	name = models.CharField(max_length = 150, blank = True, null = True)
	status = models.BooleanField(default=False)
	item = models.ForeignKey('Items', models.CASCADE, blank=True, null=True)



class Items(models.Model):

	title = models.CharField(max_length = 50, blank = True, null = True)

