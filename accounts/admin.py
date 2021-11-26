
from django.contrib import admin

# Register your models here.
from accounts.models import User,GeneralUser,TrainMaster


admin.site.register(User)

admin.site.register(GeneralUser)

admin.site.register(TrainMaster)