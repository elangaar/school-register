from django import forms
from journal.models import (Student, Employee, Position, Class_, Classroom,
                            Subject, School, Note, Grade, Parent)

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['first_name', 'second_name', 'last_name', 'pesel',
                  'which_class', 'parents']

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['first_name', 'second_name', 'last_name', 'pesel', 'position',
                  'which_class']


class PositionForm(forms.ModelForm):

    class Meta:
        model = Position
        fields = ['name', 'description']


class ClassForm(forms.ModelForm):

    class Meta:
        model = Class_
        fields = ['level', 'branch', 'classroom', 'school']


class ClassroomForm(forms.ModelForm):

    class Meta:
        model = Classroom
        fields = ['number']


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ['name', 'classroom']


class SchoolForm(forms.ModelForm):

    class Meta:
        model = School
        fields = ['name', 'type_of_school']

class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ['title', 'content', 'student']


class GradeForm(forms.ModelForm):

    class Meta:
        model = Grade
        fields = ['value', 'category', 'subject']


class ParentForm(forms.ModelForm):

    class Meta:
        model = Parent
        fields = ['first_name', 'second_name', 'last_name', 'telephone_number']

