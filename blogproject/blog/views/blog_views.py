import csv
from django.shortcuts import render
from blog.models.blog_model import *
from django.http import HttpResponse,JsonResponse
# Create your views here.

def index(request):
	response = HttpResponse(content_type='text/csv')
	filename = "blogs.csv"
	response['Content-Disposition'] = 'attachment; filename="{0}"'.format(filename)
	writer = csv.writer(response)
	for blog in Blog.objects.all():
		writer.writerow([blog.blog_name, blog.blog_description])

	return response
