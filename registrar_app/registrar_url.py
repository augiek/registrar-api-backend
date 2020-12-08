from django.urls import path
from . import views

urlpatterns = [
    path('students', views.student_list, name="student_list"),
    path('students/new', views.new_student, name="new_student"),
    path('students/<int:student_id>', views.student_detail, name="student_detail"),
    path('students/<int:student_id>/edit', views.edit_student, name="edit_student"),
    path('students/<int:student_id>/delete', views.delete_student, name="delete_student"),
        
    path('courses/', views.course_list, name="course_list"),
    path('courses/<int:course_id>', views.course_detail name="course_detail"),
    path('courses/<int:course_id>/edit', views.edit_course, name="edit_course"),
    path('courses/<int:course_id>/delete', views.delete_course, name="delete_course"),
    path('courses/<int:course_id>/enroll/<int:student_id>', views.delete_course, name="delete_course"),
    path('courses/<int:course_id>/drop/<int:student_id>', views.drop_student, name="drop_student"),


    # path('<int:student_id>/courses', views.student_courselist, name="student_courselist"),
    # path('courses/<int:course_id>/students', views.course_enrollment, name="course_enrollment"),


]