from django.contrib import admin

from mainweb.models import Book,Contact

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('name','meal','capacity')
    ordering=['date']
    search_fields=['name']







admin.site.register(Book,BookAdmin)
admin.site.register(Contact)



