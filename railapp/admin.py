from django.contrib import admin
from .models import Questions, Answers, Station, Train, TrainSchedule

# Register your models here.
from railapp.models import Contact




class AnswerInline(admin.TabularInline):
    model = Answers

class QuestionsAdmin(admin.ModelAdmin):

    inlines = [AnswerInline]
    class Meta:
        model = Questions


admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Answers)
admin.site.register(Contact)
admin.site.register(Station)
admin.site.register(Train)
admin.site.register(TrainSchedule)

