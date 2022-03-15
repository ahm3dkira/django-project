from django.shortcuts import render

# Create your views here.

def index(request):
    # render the index page
    return render(request, 'index.html')

def courses(request):
    # render the courses page
    return render(request, 'courses.html')

def course(request, course):
    # render the course page
    return render(request, 'course.html', {'course_name': course})

