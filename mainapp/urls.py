# first create the file urls in the app

# import the views from the same directorie

from . import views
from django.urls import path


app_name = "main"

urlpatterns = [
	path('inicio/',views.index,name='index'),
	path('',views.index,name='index'),
	path('downloads/',views.downloads,name="downloads"),
	path('esto/',views.downloads,name="downloads"),
	]



