from django.conf.urls import url

# from .views import StudentListView
from .views import student_list, ClassListView, ClassDetailView

urlpatterns = [
#    url(r'^list/$', StudentListView.as_view(), name='student-list'),
    url(r'^list/students/$', student_list, name='student-list'),
    url(r'^list/class/$', ClassListView.as_view(), name='class-list'),
    url(r'^list/class/(?P<slug>\d{1}-\w{1})/$', ClassDetailView.as_view(),
    name='class-detail'),
]
