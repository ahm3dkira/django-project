from django.shortcuts import render
from django.http import HttpResponse
from .models import Course

# Create your views here.

def index(request):
    # render the index page
    return render(request, 'index.html')

def courses(request):
    # render the courses page
    return render(request, 'courses.html')

coursesData = [
    {
        'id': '1',
        'title': 'Data structures | Dr. khaled',
        'description': 'Data structures are the foundation of computer science. They are the building blocks of almost all other computer science concepts.',
        'image': 'data.png',
        'time': '12 weeks',
        'type': 'acadimc',
        'votes': '100',
        'files': [
            "http://localhost:3000/55.pdf",
            "http://localhost:3000/55888.pdf",
            "http://localhost:3000/5dcdv55.pdf",
        ]
    },
    {
        'id': '2',
        'title': 'Algorithms | Dr. khaled',
        'description': 'Algorithms are the foundation of computer science. They are the building blocks of almost all other computer science concepts.',
        'image': 'algo.png',
        'time': '12 weeks',
        'votes': '100',
        'files': [
            "http://localhost:3000/uuuuu.pdf",
            "http://localhost:3000/55888.pdf",
            "http://localhost:3000/5dcdv55.pdf",
        ]
    },
    {
        'id': '3',
        'title': 'Operating Systems | Dr. moahmed',
        'description': 'Operating systems are the foundation of computer science. They are the building blocks of almost all other computer science concepts.',
        'image': 'os.png',
        'time': '12 weeks',
        'votes': '100',
        'files': [
            "http://localhost:3000/55.pdf",
            "http://localhost:3000/85888.pdf",
            "http://localhost:3000/5dcdv55.pdf",
        ]
    },

    
]

def allCourses(request):
    return render(request, 'allCourses.html', {'courses': coursesData})
def course(request, course):
    for i in coursesData:
        if i['id'] == course:
            return render(request, 'course.html', {'course': i})
    return HttpResponse('Course not found')

def removeCourse(request, course):
    for i in coursesData:
        if i['id'] == course:
            coursesData.remove(i)
            return HttpResponse('Course removed')
    return HttpResponse('Course not found')

