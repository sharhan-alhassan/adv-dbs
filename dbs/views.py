from django.shortcuts import render
from .models import Student, Course, ReportCard
from .forms import Register
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
""""
home -- form 
home -- a card of each student 
"""
def home(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = Register(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('/')
        else:
            messages.error(request, 'Invalid form!')
    else:
        form = Register()

    context = {
        'students': students,
        'form': form,
    }

    return render(request, 'dbms/home.html', context)


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student_course = student.course
    report = get_object_or_404(ReportCard, course=student_course)
    print(report.course)

    context = {
        'student': student,
    }

    return render(request, 'dbms/detail.html', context)


def about(request):
    return render(request, 'dbms/about.html')