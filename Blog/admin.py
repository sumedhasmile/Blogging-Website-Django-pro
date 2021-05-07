from django.contrib import admin

# Register your models here.


from .models import *
admin.site.register(Student)
admin.site.register(Category)
admin.site.register(BlogModel)
admin.site.register(UserDetail)
admin.site.register(UserComments)