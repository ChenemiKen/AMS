from amapp.models import Register, Session, Student
from django.contrib import admin

class SessionAdmin(admin.ModelAdmin):
    #  model= Book
     filter_horizontal = ('attendees',)

# Register your models here.
admin.site.register(Student)
admin.site.register(Register)
admin.site.register(Session)