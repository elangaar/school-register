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
    url(r'^student/$', StudentListView.as_view(), name='student-list'),
    url(r'^student/(?P<slug>\w+-\w+[\w-]*)/$', StudentDetailView.as_view(), name='student-detail'),

    url(r'^class/$', ClassListView.as_view(), name='class-list'),
    url(r'^class/(?P<slug>\d{1}-\w{1})/$', ClassDetailView.as_view(),
        name='class-detail'),

    url(r'^employee/$', EmployeeListView.as_view(), name='employee-list'),
    url(r'^employee/(?P<slug>\w+-\w+[\w-]*)/$', EmployeeDetailView.as_view(), name='employee-detail'),

    url(r'^note/$', NoteListView.as_view(), name="note-detail"),
    url(r'^note/(?P<slug>[\w-]+)/$', NoteDetailView.as_view(), name='note-detail'),

    url(r'^classroom/$', ClassroomListView.as_view(), name='classroom-list'),
    url(r'^classroom/(?P<slug>\d+)/$', ClassroomDetailView.as_view(), name='classroom-detail'),

    url(r'^parent/$', ParentListView.as_view(), name='parent-list'),
    url(r'^parent/(?P<slug>\w+-\w+[\w-]*)/$', ParentDetailView.as_view(), name='parent-detail'),

    url(r'^position/$', PositionListView.as_view(), name='position-list'),
    url(r'^position/(?P<slug>\w+)/$', PositionDetailView.as_view(), name='position-detail'),

]
