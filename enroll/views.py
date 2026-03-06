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
    from django.shortcuts import render, redirect
from .models import Student, Course


def home(request):
    return render(request, "home.html")


# ---------- STUDENT ----------

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


# ---------- COURSE ----------

def add_course(request):

    if request.method == "POST":
        course_name = request.POST.get("course_name")
        course_code = request.POST.get("course_code")
        instructor = request.POST.get("instructor")

        Course.objects.create(
            course_name=course_name,
            course_code=course_code,
            instructor=instructor
        )

        return redirect("course_list")

    return render(request, "add_course.html")


def course_list(request):

    courses = Course.objects.all()

    return render(request, "course_list.html", {"courses": courses})
