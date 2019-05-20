from django.conf.urls import include ,url
from blog.views.blog_views import index
from . import views
urlpatterns = [
	url(r'^blog/',views.blog_views.index,name='index'),
]
