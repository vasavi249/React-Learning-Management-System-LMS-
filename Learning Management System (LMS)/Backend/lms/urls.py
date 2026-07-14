from django.urls import path
from . import views

urlpatterns = [
    # Students APIs
    path('students/', views.students, name='students'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/update/<str:id>/', views.update_student, name='update_student'),
    path('students/delete/<str:id>/', views.delete_student, name='delete_student'),

    # Instructors APIs
    path('instructors/', views.instructors, name='instructors'),
    path('instructors/add/', views.add_instructor, name='add_instructor'),
    path('instructors/update/<str:id>/', views.update_instructor, name='update_instructor'),
    path('instructors/delete/<str:id>/', views.delete_instructor, name='delete_instructor'),

    # Courses APIs
    path('courses/', views.courses, name='courses'),
    path('courses/add/', views.add_course, name='add_course'),
    path('courses/update/<str:id>/', views.update_course, name='update_course'),
    path('courses/delete/<str:id>/', views.delete_course, name='delete_course'),

    # Enrollments APIs
    path('enrollments/', views.enrollments, name='enrollments'),
    path('enrollments/add/', views.add_enrollment, name='add_enrollment'),
    path('enrollments/update/<str:id>/', views.update_enrollment, name='update_enrollment'),
    path('enrollments/delete/<str:id>/', views.delete_enrollment, name='delete_enrollment'),

    # Assignments APIs
    path('assignments/', views.assignments, name='assignments'),
    path('assignments/add/', views.add_assignment, name='add_assignment'),
    path('assignments/update/<str:id>/', views.update_assignment, name='update_assignment'),
    path('assignments/delete/<str:id>/', views.delete_assignment, name='delete_assignment'),
]