from django.urls import path
from Emp import views
urlpatterns=[
	path('',views.home,name='hm'),
	path('ab/',views.about,name='ab'),
	path('co/',views.contact,name='co'),
	path('lg/',views.login,name='lg'),
	path('rg/',views.register,name='rg'),
	path('cr/',views.crud,name='crud'),	
	path('dl/<str:id>',views.delt,name='delete'),
	path('df/',views.dform,name="dff"),
]