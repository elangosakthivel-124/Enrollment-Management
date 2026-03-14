from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Student, Course, Enrollment


# ---------- LOGIN ----------

def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")


# ---------- LOGOUT ----------

def user_logout(request):
    logout(request)
    return redirect("login")


# ---------- DASHBOARD ----------

@login_required
def home(request):

    total_students = Student.objects.count()
    total_courses = Course.objects.count()
    total_enrollments = Enrollment.objects.count()

    context = {
        "total_students": total_students,
        "total_courses": total_courses,
        "total_enrollments": total_enrollments
    }

    return render(request, "home.html", context)


# ---------- STUDENT LIST ----------

@login_required
def student_list(request):

    query = request.GET.get("q")

    if query:
        students = Student.objects.filter(name__icontains=query)
    else:
        students = Student.objects.all()

    return render(request, "student_list.html", {"students": students})


# ---------- COURSE LIST ----------

@login_required
def course_list(request):

    query = request.GET.get("q")

    if query:
        courses = Course.objects.filter(course_name__icontains=query)
    else:
        courses = Course.objects.all()

    return render(request, "course_list.html", {"courses": courses})


# ---------- ENROLLMENT LIST ----------

@login_required
def enrollment_list(request):

    enrollments = Enrollment.objects.select_related("student", "course")

    return render(request, "enrollment_list.html", {"enrollments": enrollments})
