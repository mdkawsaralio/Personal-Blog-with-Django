from django.contrib import admin

# Register your models here.

from .models import Book,Author,address,Country

class BookAdmin(admin. ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating",)
    list_display = ("title", "author",)


class AuthorAdmin(admin.ModelAdmin):
    list_display=("first_name","address",)
    list_filter=("first_name","last_name",)



admin.site.register(Book, BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(address)
admin.site.register(Country)