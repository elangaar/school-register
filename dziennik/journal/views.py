from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import (Student, Grade, Class_, )

# Create your views here.

# class StudentListView(ListView):
#    template_name="journal/students_list.html"
#    model = Student
#
#    def get_context_data(self, **kwargs):
#        context = super(StudentListView, self).get_context_data(**kwargs)
#        return context

CATEGORIES_OF_GRADES = ["test", "oral_answer", "homework"]
NO_GRADES_MESSAGE = "Brak ocen"


def student_grades(student):
    grades = []
    for elem in student.grades.values().values():
        grade = (elem['value'], elem['category'])
        grades.append(grade)
    return grades

def student_average(data):
    homework = []
    oral_answer =[]
    test = []
    for grade in data:
        if grade[1] == "test":
            test.append(grade[0])
        elif grade[1] == "oral_answer":
            oral_answer.append(grade[0])
        elif grade[1] == "homework":
            homework.append(grade[0])
    try:
        sum_values = (sum(test)+sum(oral_answer)+sum(homework))
        length = float(len(test)+len(oral_answer)+len(homework))
        average = round((sum_values/length), 2)
    except ZeroDivisionError:
        average = NO_GRADES_MESSAGE

    return average


def student_list(request):
    students_queryset = Student.objects.all().order_by('last_name')
    deg = []
    stud = {}
    for student in students_queryset:
        stud['first_name'] = student.first_name
        stud['last_name'] = student.last_name
        stud['grades'] = student_grades(student)
        stud['average'] = student_average(student_grades(student))
        deg.append(stud)
        stud = {}


    context = {
        'students': students_queryset,
        'students_grades': deg,
        'categories_of_grades': CATEGORIES_OF_GRADES,
    }
    return render(request, "journal/students_list.html", context)


class ClassListView(ListView):
    template_name = "journal/class_list.html"
    model = Class_


class ClassDetailView(DetailView):
    template_name = "journal/class_detail.html"
    model = Class_
