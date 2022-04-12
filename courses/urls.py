from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('id/<course>', views.course, name='courses'),
    path('id/<course>/remove', views.removeCourse, name='removeCourse'),
    path('all', views.allCourses, name='allCourses'),
    path('new', views.addCourse, name='addCourse'),
] 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
