from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=300, widget=forms.Textarea)
    image = forms.ImageField(required=False)
    price = forms.IntegerField(required=False)
    class Meta:
        model = Course
        fields = ['title', 'description', 'image']
        labels = {'title': 'Course Title', 'description': 'Course Description', 'image': 'Course Image'}
        help_texts = {'title': 'Enter the course title', 'description': 'Enter the course description', 'image': 'Enter the course image'}
        error_messages = {'title': {'required': 'Please enter the course title'}, 'description': {'required': 'Please enter the course description'}}
        


