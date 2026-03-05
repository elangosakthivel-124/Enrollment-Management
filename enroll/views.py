from django.shortcuts import render, redirect
from .models import Student


def home(request):
    return render(request, "home.html")


def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        Student.objects.create(
            name=name,
            email=email,
            phone=phone
        )

        return redirect("student_list")

    return render(request, "add_student.html")


def student_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", {"students": students})
