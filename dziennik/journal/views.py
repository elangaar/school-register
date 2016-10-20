from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Permission
from guardian.decorators import permission_required_or_403

from django.views.generic import (
    ListView, DetailView, View,
    DeleteView, UpdateView,
)

from .models import (
    Student, Grade, Class_, Note,
    Classroom, Position, School, Subject, Grade,
    Person,
)
from .forms import (
    StudentForm, NoteForm, ClassForm,
    ClassroomForm, PositionForm, SchoolForm,
    SubjectForm, GradeForm
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


#@method_decorator(permission_required_or_403('journal.view_student'), name='dispatch')
class StudentListView(ListView):
    template_name = "journal/student_list.html"
    model = Student

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['average'] = "Średnia"
        return context


#@permission_required('journal.view_student', return_403=True)
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


@method_decorator(permission_required_or_403('journal.view_student', 
                                             (Student, 'slug', 'slug'), accept_global_perms=True), name='dispatch')
class StudentDetailView(DetailView):
    template_name = "journal/student_detail.html"
    model = Student

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ClassListView(ListView):
    template_name = "journal/class_list.html"
    model = Class_


@method_decorator(login_required, name='dispatch')
class ClassDetailView(DetailView):
    template_name = "journal/class_detail.html"
    model = Class_


# class EmployeeListView(ListView):
#     template_name = "journal/employee_list.html"
#     model = Employee


# @method_decorator(login_required, name='dispatch')
# class EmployeeDetailView(DetailView):
#     template_name = "journal/employee_detail.html"
#     model = Employee


class NoteListView(ListView):
    template_name = "journal/note_list.html"

    def get_queryset(self):
        student = self.kwargs['slug']
        return Note.objects.filter(student__slug=student)


@method_decorator(login_required, name='dispatch')
class NoteDetailView(DetailView):
    template_name = "journal/note_detail.html"
    model = Note


class ClassroomListView(ListView):
    template_name = "journal/classroom_list.html"
    model = Classroom


@method_decorator(login_required, name='dispatch')
class ClassroomDetailView(DetailView):
    template_name = "journal/classroom_detail.html"
    model = Classroom

    #def get_object(self):
    #    return get_object_or_404(Classroom, pk=self.number)


# class ParentListView(ListView):
#     template_name = "journal/parent_list.html"
#     model = Parent


# @method_decorator(login_required, name='dispatch')
# class ParentDetailView(DetailView):
#     template_name = "journal/parent_detail.html"
#     model = Parent


class PositionListView(ListView):
    template_name = "journal/position_list.html"
    model = Position
    context_object_name = "position_list"


@method_decorator(login_required, name='dispatch')
class PositionDetailView(DetailView):
    template_name = "journal/position_detail.html"
    model = Position


@method_decorator(login_required, name='dispatch')
class SchoolDetailView(DetailView):
    template_name = "journal/school_detail.html"
    model = School


class SubjectListView(ListView):
    template_name = "journal/subject_list.html"
    model = Subject


@method_decorator(login_required, name='dispatch')
class SubjectDetailView(DetailView):
    template_name = "journal/subject_detail.html"
    model = Subject


class GradeDetailView(DetailView):
    template_name = "journal/grade_detail.html"
    model = Grade


@method_decorator(login_required, name='dispatch')
class UserDetailView(DetailView):
    template_name = "journal/user_detail.html"
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = 'user'
        return context

@login_required
def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('journal:student-list'))
    else:
        form = StudentForm()
    return render(request, "journal/forms/student_add.html", {'form':form})

@login_required
def note_add(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('journal:student-list'))
    else:
        form = NoteForm()
    return render(request, "journal/forms/note_add.html", {'form':form})

@login_required
def class_add(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('journal:class-list'))
    else:
        form = ClassForm()
    return render(request, "journal/forms/class_add.html", {'form':form})

@login_required
def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('journal:employee-list'))
    else:
        form = EmployeeForm()
    return render(request, "journal/forms/employee_add.html", {'form':form})

@login_required
def classroom_add(request):
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('journal:classroom-list'))
    else:
        form = ClassroomForm()
    return render(request, "journal/forms/classroom_add.html", {'form':form})

@login_required
def parent_add(request):
    if request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('journal:parent-list'))
    else:
        form = ParentForm()
    return render(request, "journal/forms/parent_add.html", {'form':form})

@login_required
def position_add(request):
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('journal:position-list'))
    else:
        form = PositionForm()
    return render(request, "journal/forms/position_add.html", {'form':form})

@login_required
def school_add(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = SchoolForm()
    return render(request, "journal/forms/school_add.html", {'form':form})

@login_required
def subject_add(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('journal:subject-list'))
    else:
        form = SubjectForm()
    return render(request, "journal/forms/subject_add.html", {'form':form})

@login_required
def grade_add(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('journal:student-list'))
    else:
        form = GradeForm()
    return render(request, "journal/forms/grade_add.html", {'form':form})


@method_decorator(login_required, name='dispatch')
class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('journal:student-list')

    def post(self, request, *args, **kwargs):
        if 'cancel' in request.POST:
            url = self.success_url
            return HttpResponseRedirect(url)
        else:
            return super().post(self, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class StudentUpdateView(UpdateView):
    model = Student
    fields = [
        'first_name', 'second_name', 'last_name', 'pesel',
        'which_class', 'grades', 'parents',
    ]
    template_name_suffix = '_update_form'



from django.http import HttpResponse

def my_view(request):
    if request.method == "GET":
        return HttpResponse("Wynik GET z widoku")

class MyView(View):
    def get(self, request):
        return HttpResponse("Wynik GET z MyWiew")


class PersonDetailView(DetailView):
    model = Person
    template_name = "journal/person_detail.html"
