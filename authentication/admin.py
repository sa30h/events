from django.contrib import admin
from .models import SubUser,Task,TaskUpdates,Comment,EventTask,TaskComment



# Register your models here.
admin.site.register(SubUser)
admin.site.register(Task)
admin.site.register(TaskUpdates)
admin.site.register(Comment)
admin.site.register(TaskComment)
admin.site.register(EventTask)