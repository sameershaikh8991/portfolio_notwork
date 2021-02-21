from django.db import models

# Create your models here.

class Myproject(models.Model):
	Pname = models.CharField(max_length=50)
	Ptag = models.TextField(max_length=20)
	Pimage = models.ImageField(upload_to="main/images",default="")
	Purl = models.URLField(max_length=500, blank=True)

	def __str__(self):
		return self.Pname
