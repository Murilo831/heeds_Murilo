from django.contrib import admin
from .models import Search

'''
admin.site.register(Search)
'''
@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    list_display = ('id', 'address')



