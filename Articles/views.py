from django.shortcuts import render
# Create your views here.
# # for rendering html and to redirect into an other page
from django.shortcuts import render,redirect,get_object_or_404
from .models import Article,Category

def Documentation(request):
	ListOfArticles = Article.objects.all()
	dic = {}
	dic["ListOfArticles"] = ListOfArticles
	dic["Header"] = "Documentation"
	return render(request,'Articles/index.html',dic)

def AllArticles(request):
	ListOfArticles = Article.objects.all()
	dic = {}
	dic["ListOfArticles"] = ListOfArticles
	dic["Header"] = "Wiki"
	return render(request,'Articles/index.html',dic)

def detail(request,article_id):
	dic = {}
	dic['id'] = article_id
	article = get_object_or_404(Article,pk=article_id)
	dic['article'] = article
	dic['categories'] = article.categories.all()
	colors = [
			'#FFB000',
			'#FFDE00',
			'#1DFF00',
			'#FFFFFF',
			'#00FFDB',
			'#002BFF',
			'#7A00FF',
			]
	categories_color = []
	counter = 0
	for category in dic['categories']:
		categories_color.append({"object":category,"color":colors[counter%len(colors)]})
		counter+=1
	dic['categories'] = categories_color
	return render(request,'Articles/detail.html',dic)





