# first create the file urls in the app

# import the views from the same directorie

from . import views
from django.urls import path
from django.conf import settings


from django.conf.urls.static import static

#


app_name = "article"

urlpatterns = [
	path('Documentation/',views.Documentation,name='Documentation'),
	path('',views.AllArticles,name='AllArticles'),
	path('id/<int:article_id>/',views.detail,name = 'detail'),
	]



