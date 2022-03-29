from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index, name='index'),
    # path('about/', views.about, name='about'),
    # path('courses/', include('courses.urls'), name='courses'),
    # path('blog/', include('blog.urls'), name='blog'),
    path('', include('courses.urls'), name='courses'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

