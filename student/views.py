from django.shortcuts import render
from student.models import Student
from .forms import StudentForm
# Create your views here.

def studentview(request):
    context = {}
    context['form']=StudentForm()
    #student_list = Student.objects.order_by('marks')
    #return render(request, 'student.html',{'student_list':student_list})
    return render(request, 'input.html',context)