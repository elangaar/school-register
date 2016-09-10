from django.shortcuts import render

from django.views.generic import ListView

from .models import (Student, Degree, )

# Create your views here.

# class StudentListView(ListView):
#    template_name="journal/students_list.html"
#    model = Student
#
#    def get_context_data(self, **kwargs):
#        context = super(StudentListView, self).get_context_data(**kwargs)
#        return context

CATEGORIES_OF_DEGREES = ["test", "oral_answer", "homework"]

def student_degrees(student):
    degrees = []
    for elem in student.degrees.values().values():
        degree = (elem['value'], elem['category'])
        degrees.append(degree)
    return degrees

def student_average(data):
    homework = []
    oral_answer =[]
    test = []
    for degree in data:
        if degree[1] == "test":
            test.append(degree[0])
        elif degree[1] == "oral_answer":
            oral_answer.append(degree[0])
        elif degree[1] == "homework":
            homework.append(degree[0])
    sum_values = (sum(test)*1.0+sum(oral_answer)*0.8+sum(homework)*0.6)
    length = float(len(test)+len(oral_answer)+len(homework))
    average = round((sum_values/length), 2)

    return average


def student_list(request):
    students_queryset = Student.objects.all()
    deg = []
    stud = {}
    for student in students_queryset:
        stud['first_name'] = student.first_name
        stud['last_name'] = student.last_name
        stud['degrees'] = student_degrees(student)
        stud['average'] = student_average(student_degrees(student))
        deg.append(stud)
        stud = {}


    context = {
        'students': students_queryset,
        'students_degrees': deg,
        'categories_of_degrees': CATEGORIES_OF_DEGREES, 
    }
    return render(request, "journal/students_list.html", context)


