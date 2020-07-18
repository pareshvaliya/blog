from django.db import models
#User model is readily available so it is imported
from django.contrib.auth.models import User

# Create your models here.
class UserTimeStamp(models.Model):
	#auto_now_add 
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	# Table of this class is not created in data base
	# by writing below class
	# because UserTimeStamp is inherited in Post so no need to create here
	class Meta:
		abstract = True

class Post(UserTimeStamp):
	#charfield consist of everything(number, alpha,special char etc.)
	title = models.CharField(max_length = 100)
	description = models.TextField()
	image = models.ImageField(upload_to = 'post') # upload in /meadia/post folder
	#created_by = models.CharField(max_length = 50)
	likes = models.IntegerField(default = 0)

	def __str__(self): # it is like toString method
		return self.title

class Comment(UserTimeStamp):
 	post = models.ForeignKey(Post, on_delete = models.CASCADE)
 	comment = models.TextField() 