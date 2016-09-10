from django.contrib import admin

from journal.models import (Employee,
                            Position,
                            Class_,
                            Classroom,
                            School,
                            Subject,
                            Student,
                            Degree,
                            Note,
                            Parent
)

# Register your models here.

admin.site.register(Employee)
admin.site.register(Position)
admin.site.register(Class_)
admin.site.register(Classroom)
admin.site.register(School)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Degree)
admin.site.register(Note)
admin.site.register(Parent)

