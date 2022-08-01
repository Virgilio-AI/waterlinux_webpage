from django.db import models

# Create your models here.




from ckeditor.fields import RichTextField
# import the user table
from django.contrib.auth.models import User

# table named Category 
class Category(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=255,)
	created_at = models.DateTimeField(auto_now_add=True)
	# father = models.ForeignKey('self',on_delete=models.CASCADE)

	# the name to be printed
	def __str__(self):
		return self.name

class Article(models.Model):
	title = models.CharField(max_length=150)
	content = RichTextField()
	public = models.BooleanField()
	# foreign key to create relationship many to one
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	# many to many relationship between Category and Article
	categories = models.ManyToManyField(Category,blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title
