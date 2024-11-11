from django.contrib import admin
from .models import Blog, Category, Tag, Menu, Comment, CustomUser

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Menu)
admin.site.register(Comment)
admin.site.register(CustomUser)
