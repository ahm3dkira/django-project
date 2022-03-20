from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('id/<course>', views.course, name='courses'),
    path('id/<course>/remove', views.removeCourse, name='removeCourse'),
    path('all', views.allCourses, name='allCourses'),
]
