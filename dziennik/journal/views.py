from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.views.generic import ListView, DetailView, View

from .models import (Student, Grade, Class_, Employee, Note, 
                     Classroom, Parent, Position
                    )

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


class StudentListView(ListView):
    template_name = "journal/student_list.html"
    model = Student
    # paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['average'] = "Średnia"
        return context


def student_list(request):
    students_queryset = Student.objects.filter().order_by('last_name')
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
    return render(request, "journal/student_list.html", context)


class StudentDetailView(DetailView):
    template_name = "journal/student_detail.html"
    model = Student


class ClassListView(ListView):
    template_name = "journal/class_list.html"
    model = Class_


class ClassDetailView(DetailView):
    template_name = "journal/class_detail.html"
    model = Class_


class EmployeeListView(ListView):
    template_name = "journal/employee_list.html"
    model = Employee


class EmployeeDetailView(DetailView):
    template_name = "journal/employee_detail.html"
    model = Employee


class NoteListView(ListView):
    template_name = "journal/note_list.html"
    model = Note


class NoteDetailView(DetailView):
    template_name = "journal/note_detail.html"
    model = Note


class ClassroomListView(ListView):
    template_name = "journal/classroom_list.html"
    model = Classroom


class ClassroomDetailView(DetailView):
    template_name = "journal/classroom_detail.html"
    model = Classroom

    #def get_object(self):
    #    return get_object_or_404(Classroom, pk=self.number)


class ParentListView(ListView):
    template_name = "journal/parent_list.html"
    model = Parent


class ParentDetailView(DetailView):
    template_name = "journal/parent_detail.html"
    model = Parent


class PositionListView(ListView):
    template_name = "journal/position_list.html"
    model = Position
    context_object_name = "position_list"


class PositionDetailView(DetailView):
    template_name = "journal/position_detail.html"
    model = Position

from django.http import HttpResponse

def my_view(request):
    if request.method == "GET":
        return HttpResponse("Wynik GET z widoku")

class MyView(View):
    def get(self, request):
        return HttpResponse("Wynik GET z MyWiew")
