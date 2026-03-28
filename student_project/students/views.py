from django.shortcuts import render, redirect
from .models import Student

def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})

def add_student(request):
    if request.method == "POST":
        name = request.POST['name']
        roll = request.POST['roll']
        email = request.POST['email']
        course = request.POST['course']

        Student.objects.create(
            name=name,
            roll=roll,
            email=email,
            course=course
        )

        return redirect('/')

    return render(request, 'add.html')
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/')

def edit_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        student.name = request.POST['name']
        student.roll = request.POST['roll']
        student.email = request.POST['email']
        student.course = request.POST['course']
        student.save()
        return redirect('/')

    return render(request, 'edit.html', {'student': student})