from django.contrib import admin

# Register your models here.

from .models import Users,Roles,User_role,Courses,Assitens,Notes,Estate,Certificates

admin.site.register(Users)
admin.site.register(Roles)
admin.site.register(User_role)
admin.site.register(Courses)
admin.site.register(Assitens)
admin.site.register(Notes)
admin.site.register(Estate)
admin.site.register(Certificates)
