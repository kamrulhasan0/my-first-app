from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 

class Blog(models.Model):
	title = models.CharField(max_length = 200)
	content = models.TextField()
	author  = models.ForeignKey(User, on_delete = models.CASCADE)

	def get_absolute_url(self):
		return reverse('blog:detail', kwargs ={'pk':self.pk})