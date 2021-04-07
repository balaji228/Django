from django.urls import path
from balaji import views

urlpatterns = [
	path('',views.home),
	path('demo/',views.chk),
	path('da/',views.home),
	path('gb/',views.login),
	path('rg/',views.reg),
]