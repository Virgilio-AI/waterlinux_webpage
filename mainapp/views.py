# Date: 24/March/2022 - Thursday
# Author: Virgilio Murillo Ochoa
# personal github: Virgilio-AI
# linkedin: https://www.linkedin.com/in/virgilio-murillo-ochoa-b29b59203
# contact: virgiliomurilloochoa1@gmail.com


# # for rendering html and to redirect into an other page
from django.shortcuts import render,redirect
# # for poping messages
from django.contrib import messages
# Create your views here.
from .models import IsoFile

# to create a view just add
def index(request):
	dic = {}
	return render(request,'MainApp/index.html',dic)

def downloads(request):
	dic = {}

	# inside a view
	downloads = IsoFile.objects.all()
	cont=0
	for download in downloads:
		cont+=1
		download.created_at = download.created_at.strftime('%B %d, %Y')
		download.updated_at = download.updated_at.strftime('%B %d, %Y')
		download.index = cont

	dic['downloads'] = downloads


	return render(request,'MainApp/downloads.html',dic)
