from django.db import models

# Create your models here.

class Categories(models.Model):
	categories_id = models.PositiveSmallIntegerField(primary_key="true", null=False, default=0)
	categorie_name = models.CharField(max_length=64, null=True, blank=True)

	def __str__(self):
		return self.categorie_name



class Blog(models.Model):
	blog_id = models.AutoField(primary_key="true")
	categories_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
	blog_name = models.CharField(max_length=16, null=True, blank=True)
	blog_description = models.CharField(max_length=64, null=True, blank=True)
	created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_on = models.DateTimeField(auto_now=True, auto_now_add=False)
	created_by = models.CharField(max_length=50, editable=False)
	modified_by = models.CharField(max_length=50, editable=False)

	def __str__(self):
		return self.blog_name

