from django.contrib import admin
from blogapp.models import Post,Comment

# Register your models here.
class postadmin(admin.ModelAdmin):
    list_display=['id','title','slug','author','body','publish','created','updated','status']
    prepopulated_fields={'slug':('title',)}
    list_filter=('author','status','publish',)
    search_fields=('title','body',)
    raw_id_fields=('author',)

class commentadmin(admin.ModelAdmin):
    list_display=['name','email','body','post','created','updated','active']
    list_filter=('name','created','body',)
    search_fields=('body','name',)
admin.site.register(Post,postadmin)
admin.site.register(Comment,commentadmin)
