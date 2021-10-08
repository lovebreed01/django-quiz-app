from django.contrib import admin
from .models import Question,Choice,Category

class QuestionChoiceAdmin(admin.TabularInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
    inlines = [QuestionChoiceAdmin]
    
    

admin.site.register(Question , QuestionAdmin)
admin.site.register(Category)
# Register your models here.
