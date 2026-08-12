from django.contrib import admin
from . models import Author,Post,Tag

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":('title',)}
    list_display=('title','author','date')
    list_filter=('title','author','tags','date',)






admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)