from django.db import models


# Constants

DEFAULT_ID = 1

# Create your models here.
	
class Tutor(models.Model):
	first_name = models.CharField(max_length = 100, blank=True)
	last_name = models.CharField(max_length = 100, blank=True)
	about = models.TextField(blank=True)
	image = models.ImageField(upload_to='img/tutor-img/', blank=True)
	linkedin = models.CharField(max_length = 100, blank=True)
	facebook = models.CharField(max_length = 100, blank=True)
	telegram = models.CharField(max_length = 100, blank=True)
	email = models.CharField(max_length = 100, blank=True)
	
	def __str__(self):
		return self.first_name + ' ' + self.last_name
	
class Category(models.Model):
	title = models.CharField(max_length=200, blank=True)
	
	def __str__(self):
		return self.title
	
	def get_category():
		return Category.objects.get_or_create(id=1)[0]
	
class Course(models.Model):
	
	title = models.CharField(max_length = 500)
	image = models.ImageField(upload_to='img/course-img', blank=True, default='img/course-img/default.jpg')
	instructor = models.CharField(max_length = 100)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, default='1', null=True)
	duration_hour = models.CharField(max_length = 10, blank=True, default='0')
	duration_min = models.CharField(max_length = 10, blank=True, default='0')
	tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, blank=True)
	description = models.TextField()
	
	start_date = models.DateTimeField(blank=True)
	end_date = models.DateTimeField(blank=True)
	published_date = models.DateTimeField(blank = True)
	
	FAQs = models.TextField(blank=True)
	
	enroll = models.CharField(max_length=500, blank=True)
	
	def publish(self):
		self.save()
	
	def get_FAQs(self):
		FAQs_list = []
		for line in self.FAQs.splitlines():
			FAQs_list.append(line.split(':'))
		return FAQs_list
		
	
	def __str__(self):
		return self.title

	
	
	
	
	
	
	