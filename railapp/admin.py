
from django.contrib import admin
from railapp.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=('id','firstname','lastname','username', 'email','phone','gender','password')
admin.site.register(User,UserAdmin)