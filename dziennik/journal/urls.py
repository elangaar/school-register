from django.conf.urls import url

# from .views import StudentListView
from .views import student_list

urlpatterns = [
#    url(r'^list/$', StudentListView.as_view(), name='student-list'),
    url(r'^list/$', student_list, name='student-list'),
]
