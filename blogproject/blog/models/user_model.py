from django.db import models

# Create your models here.

class User_role(models.Model):
	user_role_id = models.PositiveSmallIntegerField(primary_key="true", null=False, default=0)
	user_role_name = models.CharField(max_length=64, null=True, blank=True)

	def __str__(self):
		return self.user_role_name




class User(models.Model):
	user_id = models.AutoField(primary_key="true")
	user_role_id = models.ForeignKey(User_role, on_delete=models.CASCADE)	
	name = models.CharField(max_length=16, null=True, blank=True)

	def __str__(self):
		return self.name

