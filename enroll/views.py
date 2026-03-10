from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course, Enrollment


def home(request):
    return render(request, "home.html")


# -------- STUDENT --------

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


def edit_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.phone = request.POST.get("phone")

        student.save()

        return redirect("student_list")

    return render(request, "edit_student.html", {"student": student})


def delete_student(request, id):

    student = get_object_or_404(Student, id=id)
    student.delete()

    return redirect("student_list")


# -------- COURSE --------

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


def edit_course(request, id):

    course = get_object_or_404(Course, id=id)

    if request.method == "POST":

        course.course_name = request.POST.get("course_name")
        course.course_code = request.POST.get("course_code")
        course.instructor = request.POST.get("instructor")

        course.save()

        return redirect("course_list")

    return render(request, "edit_course.html", {"course": course})


def delete_course(request, id):

    course = get_object_or_404(Course, id=id)
    course.delete()

    return redirect("course_list")


# -------- ENROLLMENT --------

def enroll_student(request):

    students = Student.objects.all()
    courses = Course.objects.all()

    if request.method == "POST":

        student_id = request.POST.get("student")
        course_id = request.POST.get("course")

        Enrollment.objects.create(
            student_id=student_id,
            course_id=course_id
        )

        return redirect("enrollment_list")

    return render(request, "enroll_student.html", {
        "students": students,
        "courses": courses
    })


def enrollment_list(request):

    enrollments = Enrollment.objects.select_related("student", "course")

    return render(request, "enrollment_list.html", {"enrollments": enrollments})
