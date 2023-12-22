from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    student_teacher = Student.objects.prefetch_related('teachers').order_by('group')
    context = {"object_list": student_teacher}

    return render(request, template, context)
