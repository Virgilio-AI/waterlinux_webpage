from django.db import models

# Create your models here.
class IsoFile(models.Model):
	file = models.FileField(upload_to='media',blank=True)
	torrent = models.CharField(max_length=1000,default="NoLink")
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

