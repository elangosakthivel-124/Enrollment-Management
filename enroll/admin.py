from django.contrib import admin
from .models import Student, Course, Enrollment


admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)

from django.contrib import admin
from .models import Student, Course, Enrollment


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "phone", "created_at")
    search_fields = ("name", "email")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "course_name", "course_code", "instructor", "created_at")
    search_fields = ("course_name", "course_code")


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "course", "enrolled_on")
