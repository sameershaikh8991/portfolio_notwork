from django.urls import path  
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('project1/',views.project1,name='project1'),
	path('search/',views.search,name='search'),
	path('footer/',views.footer, name='footer'),
	]