from django.shortcuts import render, get_object_or_404
from . import models

# Create your views here.
def index(request):
	courses = models.Course.objects.all
	tutors = models.Tutor.objects.all
	return render(request, 'index.html', {'courses':courses, 'tutors':tutors})
	
def course_detail(request, pk):
	models.Course.objects.get(pk=pk)
	course = get_object_or_404(models.Course, pk=pk)
	return render(request, 'single-course.html', {'course': course})
	


	
	
	