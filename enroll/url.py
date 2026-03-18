from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),

    # Dashboard
    path("", views.home, name="home"),

    # Students CRUD
    path("students/", views.student_list, name="student_list"),
    path("students/add/", views.student_add, name="student_add"),
    path("students/edit/<int:pk>/", views.student_edit, name="student_edit"),
    path("students/delete/<int:pk>/", views.student_delete, name="student_delete"),

    # Courses CRUD
    path("courses/", views.course_list, name="course_list"),
    path("courses/add/", views.course_add, name="course_add"),
    path("courses/edit/<int:pk>/", views.course_edit, name="course_edit"),
    path("courses/delete/<int:pk>/", views.course_delete, name="course_delete"),

    # Enrollments (list + simple create)
    path("enrollments/", views.enrollment_list, name="enrollment_list"),
    path("enrollments/enroll/", views.enroll_student, name="enroll_student"),
]
