from django.urls import path
from balaji import views

urlpatterns = [
	path('rt/',views.home,name="home"),
	path('demo/',views.chk),
	path('da/',views.home),
	path('gb/',views.login),
	path('rg/',views.reg),
	path('',views.bthm),
	path('about/',views.about,name="about"),
	path('contact/',views.contact,name="contact"),
]