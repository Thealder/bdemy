from django.urls import path
from bdemy_app import views


urlpatterns = [	
	path('', views.index, name='index'),
	path('course/<int:pk>/', views.course_detail, name='course_detail')
	

]