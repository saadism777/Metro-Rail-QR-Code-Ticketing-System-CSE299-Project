
from django.contrib import admin

# Register your models here.
from accounts.models import User,GeneralUser,TrainMaster, Route, Book


admin.site.register(User)

admin.site.register(GeneralUser)

admin.site.register(TrainMaster)

admin.site.register(Route)
admin.site.register(Book)
# admin.site.register(Ticket)