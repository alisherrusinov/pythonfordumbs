from django.contrib import admin
from .models import LessonModel, TimeCodeModel, AttachedLinkModel
# Register your models here.
admin.site.register(LessonModel)
admin.site.register(TimeCodeModel)
admin.site.register(AttachedLinkModel)