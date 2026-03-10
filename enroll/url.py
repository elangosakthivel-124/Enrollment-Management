from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name="home"),

    path("add-student/", views.add_student, name="add_student"),
    path("students/", views.student_list, name="student_list"),
    path("edit-student/<int:id>/", views.edit_student, name="edit_student"),
    path("delete-student/<int:id>/", views.delete_student, name="delete_student"),

    path("add-course/", views.add_course, name="add_course"),
    path("courses/", views.course_list, name="course_list"),
    path("edit-course/<int:id>/", views.edit_course, name="edit_course"),
    path("delete-course/<int:id>/", views.delete_course, name="delete_course"),

    path("enroll/", views.enroll_student, name="enroll_student"),
    path("enrollments/", views.enrollment_list, name="enrollment_list"),
]
