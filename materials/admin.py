from django.contrib import admin
from .models import Items, Review


class ReviewInline(admin.TabularInline):
    model = Review

class ItemAdmin(admin.ModelAdmin):
    inlines = [ReviewInline,]
    list_display = ('title', 'author', 'price',) 


admin.site.register(Items, ItemAdmin)