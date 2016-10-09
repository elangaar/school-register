from django.conf.urls import url
from .views import (
    ClassListView, ClassDetailView,
    StudentListView, StudentDetailView,
    EmployeeListView, EmployeeDetailView,
    NoteListView, NoteDetailView,
    ClassroomListView, ClassroomDetailView,
    ParentListView, ParentDetailView,
    PositionListView, PositionDetailView,
    SchoolDetailView,
    SubjectListView, SubjectDetailView,
    GradeDetailView,
    UserDetailView,
    StudentDeleteView, StudentUpdateView,
)
from .views import (
    student_add, note_add, class_add, employee_add,
    classroom_add, parent_add, position_add, school_add,
    subject_add, grade_add
)

app_name='journal'
urlpatterns = [
    url(r'^student/$', StudentListView.as_view(), name='student-list'),
    url(r'^student/(?P<slug>\w+-\w+[\w-]*)/$',
        StudentDetailView.as_view(), 
        name='student-detail'
    ),
    url(r'^student/(?P<slug>\w+-\w+[\w-]*)/notes/$',
        NoteListView.as_view(), 
        name='note-list'
    ),
    url(r'^student/add/$', student_add, name='student-add'),
    url(r'^note/add/$', note_add, name='note-add'),
    url(r'^note/(?P<slug>[\w-]+)/$', NoteDetailView.as_view(), name='note-detail'),

    url(r'^class/$', ClassListView.as_view(), name='class-list'),
    url(r'^class/(?P<slug>\d{1}-\w{1})/$', ClassDetailView.as_view(),
        name='class-detail'),
    url(r'^class/add/$', class_add, name='class-add'),

    url(r'^employee/$', EmployeeListView.as_view(), name='employee-list'),
    url(r'^employee/(?P<slug>\w+-\w+[\w-]*)/$',
        EmployeeDetailView.as_view(), name='employee-detail'),
    url(r'^employee/add/$', employee_add, name='employee-add'),

    url(r'^classroom/$', ClassroomListView.as_view(), name='classroom-list'),
    url(r'^classroom/(?P<slug>\d+)/$',
        ClassroomDetailView.as_view(), 
        name='classroom-detail'
    ),
    url(r'^classroom/add/$', classroom_add, name='classroom-add'),

    url(r'^parent/$', ParentListView.as_view(), name='parent-list'),
    url(r'^parent/(?P<slug>\w+-\w+[\w-]*)/$',
        ParentDetailView.as_view(), 
        name='parent-detail'
    ),
    url(r'^parent/add/$', parent_add, name='parent-add'),

    url(r'^position/add/$', position_add, name='position-add'),
    url(r'^position/$', PositionListView.as_view(), name='position-list'),
    url(r'^position/(?P<slug>\w+)/$', PositionDetailView.as_view(), name='position-detail'),

    url(r'^school/add/$', school_add, name='school-add'),
    url(r'^school/(?P<slug>[\w-]+)/$', SchoolDetailView.as_view(), name='school-detail'),

    url(r'^subject/add/$', subject_add, name='subject-add'),
    url(r'^subject/$', SubjectListView.as_view(), name='subject-list'),
    url(r'^subject/(?P<slug>[\w-]+)/$', 
        SubjectDetailView.as_view(),
        name='subject-detail'
    ),

    url(r'^grade/(?P<pk>\d+)/$', GradeDetailView.as_view(), name='grade-detail'),
    url(r'^grade/add/$', grade_add, name='grade-add'),
    url(r'^user/(?P<pk>[\d]+)/$', UserDetailView.as_view(), name='user-detail'),

    url(r'^student/delete/(?P<slug>\w+-\w+[\w-]*)/$', 
        StudentDeleteView.as_view(), 
        name='student-delete'
    ),
    url(r'^student/update/(?P<slug>\w+-\w+[\w-]*)/$', 
        StudentUpdateView.as_view(), 
        name='student-update'
    ),
]

