from django.contrib import admin
from .models import Announcement,Question,Answer

# Register your models here.
from railapp.models import Contact
admin.site.register(Contact)
admin.site.register(Announcement)
admin.site.register(Question)
admin.site.register(Answer)
