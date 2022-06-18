from django.contrib import admin
from . models import User, Question, Company,ES
# Register your models here.

admin.site.register(User)
admin.site.register(Question)
admin.site.register(Company)
admin.site.register(ES)