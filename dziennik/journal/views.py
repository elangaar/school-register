from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from django.views.generic import ListView, DetailView, View

from .models import (Student, Grade, Class_, Employee, Note,
                     Classroom, Parent, Position, School, Subject, Grade,
                    )
from .forms import (StudentForm, NoteForm, ClassForm, EmployeeForm,
                    ClassroomForm, ParentForm, PositionForm, SchoolForm,
                    SubjectForm, GradeForm)


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

    def get_queryset(self):
        student = self.kwargs['slug']
        return Note.objects.filter(student__slug=student)

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


class SchoolDetailView(DetailView):
    template_name = "journal/school_detail.html"
    model = School


class SubjectListView(ListView):
    template_name = "journal/subject_list.html"
    model = Subject


class SubjectDetailView(DetailView):
    template_name = "journal/subject_detail.html"
    model = Subject


class GradeDetailView(DetailView):
    template_name = "journal/grade_detail.html"
    model = Grade


def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('journal:student-list'))
    else:
        form = StudentForm()
    return render(request, "journal/forms/student_add.html", {'form':form})

def note_add(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('journal:student-list'))
    else:
        form = NoteForm()
    return render(request, "journal/forms/note_add.html", {'form':form})

def class_add(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('journal:class-list'))
    else:
        form = ClassForm()
    return render(request, "journal/forms/class_add.html", {'form':form})

def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('journal:employee-list'))
    else:
        form = EmployeeForm()
    return render(request, "journal/forms/employee_add.html", {'form':form})

def classroom_add(request):
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('journal:classroom-list'))
    else:
        form = ClassroomForm()
    return render(request, "journal/forms/classroom_add.html", {'form':form})

def parent_add(request):
    if request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('journal:parent-list'))
    else:
        form = ParentForm()
    return render(request, "journal/forms/parent_add.html", {'form':form})

def position_add(request):
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('journal:position-list'))
    else:
        form = PositionForm()
    return reverse(request, "journal/forms/position_add.html", {'form':form})

def school_add(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('journal:school-list'))
    else:
        form = SchoolForm()
    return reverse(request, "journal/forms/school_add.html", {'form':form})

def subject_add(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('journal:subject-list'))
    else:
        form = SubjectForm()
    return render(request, "journal/forms/subject_add.html", {'form':form})

def grade_add(request):
    if request.method == 'POST':
        form = GradeFotm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('journal:student-list'))
    else:
        form = GradeForm()
    return reverse(request, "journal/forms/grade_add.html", {'form':form})

from django.http import HttpResponse

def my_view(request):
    if request.method == "GET":
        return HttpResponse("Wynik GET z widoku")

class MyView(View):
    def get(self, request):
        return HttpResponse("Wynik GET z MyWiew")
