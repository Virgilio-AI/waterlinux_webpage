from django.contrib import admin
# Register your models here.
from .models import Article,Category



class CategoryAdmin(admin.ModelAdmin):
	pass
#	readonly_fieds = ('created_at','updated_at')
#	search_fields = ('name','description')
#	list_display = ['name','created_at']

class ArticleAdmin(admin.ModelAdmin):
	pass
#	readonly_fieds = ('user','created_at','updated_at')
#	search_fields = ('title','content','user__username','categories__name')



admin.site.register(Category,CategoryAdmin)
admin.site.register(Article,ArticleAdmin)



