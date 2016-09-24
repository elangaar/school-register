from django.conf.urls import url
from .views import (ClassListView, ClassDetailView,
                    StudentListView, StudentDetailView,
                    EmployeeListView, EmployeeDetailView,
                    NoteListView, NoteDetailView,
                    ClassroomListView, ClassroomDetailView,
                    ParentListView, ParentDetailView,
                    PositionListView, PositionDetailView,
                   )

app_name='journal'
urlpatterns = [
    url(r'^students/$', StudentListView.as_view(), name='student-list'),
    url(r'^students/(?P<slug>\w+-\w+[\w-]*)/$',
        StudentDetailView.as_view(), name='student-detail'),
    url(r'^students/(?P<slug>\w+-\w+[\w-]*)/notes/$',
        NoteListView.as_view(), name='note-list'),
    url(r'^notes//(?P<slug>[\w-]+)/$',
       NoteDetailView.as_view(), name='note-detail'),

    url(r'^classes/$', ClassListView.as_view(), name='class-list'),
    url(r'^classes/(?P<slug>\d{1}-\w{1})/$', ClassDetailView.as_view(),
        name='class-detail'),

    url(r'^employees/$', EmployeeListView.as_view(), name='employee-list'),
    url(r'^employees/(?P<slug>\w+-\w+[\w-]*)/$',
        EmployeeDetailView.as_view(), name='employee-detail'),

    url(r'^classrooms/$', ClassroomListView.as_view(), name='classroom-list'),
    url(r'^classrooms/(?P<pk>\d+)/$',
        ClassroomDetailView.as_view(), name='classroom-detail'),

    url(r'^parents/$', ParentListView.as_view(), name='parent-list'),
    url(r'^parents/(?P<slug>\w+-\w+[\w-]*)/$',
        ParentDetailView.as_view(), name='parent-detail'),

    url(r'^positions/$', PositionListView.as_view(), name='position-list'),
    url(r'^positions/(?P<slug>\w+)/$', PositionDetailView.as_view(), name='position-detail'),

]
