from django.contrib import admin
from . import models
# Register your models here.

class MovieAdmin(admin.ModelAdmin):

    # Switching fields in Admin Panel
    fields = ['release_year','title','length']
    # Adding searches to Admin Panel
    search_fields = ['title','length']
    # Adding filters to Admin Panel
    list_filter = ['release_year', 'length', 'title']
    # Adding list of fields in Admin Panel
    list_display = ['title','release_year', 'length', ]
    # Enable editing attributes 
    list_editable = ['length']


admin.site.register(models.Movie, MovieAdmin)
admin.site.register(models.Customer)
