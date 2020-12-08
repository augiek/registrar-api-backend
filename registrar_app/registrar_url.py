from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name="student_list"),
    path('new', views.new_student, name="new_student"),
    path('<int:student_id>', views.student_detail, name="student_detail"),
    path('<int:student_id>/edit', views.edit_student, name="edit_student"),
    path('<int:student_id>/delete', views.delete_student, name="delete_student"),
]