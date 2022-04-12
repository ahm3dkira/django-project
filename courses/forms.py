from django import forms

class CourseForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=300, widget=forms.Textarea)
    image = forms.ImageField(required=False)
    price = forms.IntegerField(required=False)
