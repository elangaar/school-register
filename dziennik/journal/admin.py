from django.contrib import admin

from journal.models import (Position, Class_, Classroom, School,
                            Subject, Student, Grade, Note, Person)

# class EmployeeAdmin(admin.ModelAdmin):
#    exclude = ('slug',)


class StudentAdmin(admin.ModelAdmin):
    exclude = ('slug',)


# class ParentAdmin(admin.ModelAdmin):
#     exclude = ('slug',)


class NoteAdmin(admin.ModelAdmin):
    exclude = ('slug',)


class PositionAdmin(admin.ModelAdmin):
    exclude = ('slug',)


class Class_Admin(admin.ModelAdmin):
    list_display = ('level', 'branch', 'classroom', 'school')
    exclude = ('slug',)


class SchoolAdmin(admin.ModelAdmin):
    exclude = ('slug',)


class ClassroomAdmin(admin.ModelAdmin):
    exclude = ('slug',)


class SubjectAdmin(admin.ModelAdmin):
    exclude = ('slug',)


class GradeAdmin(admin.ModelAdmin):
    exclude = ('slug',)
# Register your models here.


# admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Class_, Class_Admin)
admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Note, NoteAdmin)
# admin.site.register(Parent, ParentAdmin)
admin.site.register(Person)
