from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Student, Course, Enrollment


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "enroll/login.html")


def user_logout(request):
    logout(request)
    return redirect("login")


@login_required
def home(request):
    context = {
        "total_students": Student.objects.count(),
        "total_courses": Course.objects.count(),
        "total_enrollments": Enrollment.objects.count(),
    }
    return render(request, "enroll/home.html", context)


# ─── Students ────────────────────────────────────────

@login_required
def student_list(request):
    query = request.GET.get("q", "")
    students = Student.objects.filter(name__icontains=query).order_by("name")
    paginator = Paginator(students, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "enroll/student_list.html", {"page_obj": page_obj, "query": query})


@login_required
def student_add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        if Student.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
        else:
            Student.objects.create(name=name, email=email, phone=phone)
            messages.success(request, "Student added successfully.")
            return redirect("student_list")

    return render(request, "enroll/add_student.html")


@login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.phone = request.POST.get("phone")
        student.save()
        messages.success(request, "Student updated.")
        return redirect("student_list")
    return render(request, "enroll/edit_student.html", {"student": student})


@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted.")
        return redirect("student_list")
    return render(request, "enroll/student_confirm_delete.html", {"student": student})


# ─── Courses ─────────────────────────────────────────

@login_required
def course_list(request):
    query = request.GET.get("q", "")
    courses = Course.objects.filter(course_name__icontains=query).order_by("course_name")
    paginator = Paginator(courses, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "enroll/course_list.html", {"page_obj": page_obj, "query": query})


@login_required
def course_add(request):
    if request.method == "POST":
        name = request.POST.get("course_name")
        code = request.POST.get("course_code")
        instructor = request.POST.get("instructor")

        if Course.objects.filter(course_code=code).exists():
            messages.error(request, "Course code already exists.")
        else:
            Course.objects.create(course_name=name, course_code=code, instructor=instructor)
            messages.success(request, "Course added.")
            return redirect("course_list")

    return render(request, "enroll/add_course.html")


@login_required
def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        course.course_name = request.POST.get("course_name")
        course.course_code = request.POST.get("course_code")
        course.instructor = request.POST.get("instructor")
        course.save()
        messages.success(request, "Course updated.")
        return redirect("course_list")
    return render(request, "enroll/edit_course.html", {"course": course})


@login_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        course.delete()
        messages.success(request, "Course deleted.")
        return redirect("course_list")
    return render(request, "enroll/course_confirm_delete.html", {"course": course})


# ─── Enrollments ─────────────────────────────────────

@login_required
def enrollment_list(request):
    enrollments = Enrollment.objects.select_related("student", "course").order_by("-enrolled_on")
    paginator = Paginator(enrollments, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "enroll/enrollment_list.html", {"page_obj": page_obj})


@login_required
def enroll_student(request):
    if request.method == "POST":
        student_id = request.POST.get("student")
        course_id = request.POST.get("course")

        try:
            student = Student.objects.get(id=student_id)
            course = Course.objects.get(id=course_id)
            Enrollment.objects.create(student=student, course=course)
            messages.success(request, f"{student.name} enrolled in {course.course_name}.")
        except Exception as e:
            messages.error(request, "Enrollment failed. Possibly duplicate or invalid data.")
        return redirect("enrollment_list")

    students = Student.objects.all().order_by("name")
    courses = Course.objects.all().order_by("course_name")
    return render(request, "enroll/enroll_student.html", {"students": students, "courses": courses})
