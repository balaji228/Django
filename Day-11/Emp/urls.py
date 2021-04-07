from django.urls import path
from Emp import views
urlpatterns=[
	path('',views.home,name='hm'),
	path('ab/',views.about,name='ab'),
	path('co/',views.contact,name='co'),
	path('lg/',views.login,name='lg'),
	path('rg/',views.register,name='rg'),	
]