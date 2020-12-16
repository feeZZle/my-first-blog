from django.db import models

from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model): # define Post model (with class) to save it in database with models.Model (Post is a Django Model)
	# this is a link to another model
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
	# to define text with a limited number of characters	
	title = models.CharField(max_length=200)
	# this is for long text without a limit.
	text = models.TextField()
	# this is a date and time
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)


	def publish(self): # a method to publish the post
		self.published_date = timezone.now()
		self.save()

	def __str__(self): # when it is called, we will get a text (string) with a Post title.
		return self.title
		

