from django.contrib import admin
from blog.models.blog_model import Categories,Blog
from blog.models.user_model import User_role,User
# Register your models here.
admin.site.register(Categories)
admin.site.register(Blog)
admin.site.register(User_role)
admin.site.register(User)
