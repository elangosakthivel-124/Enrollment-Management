from django.urls import path
from . import views

urlpatterns = [

    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),

    path("", views.home, name="home"),

    path("students/", views.student_list, name="student_list"),
    path("courses/", views.course_list, name="course_list"),
    path("enrollments/", views.enrollment_list, name="enrollment_list"),

]
