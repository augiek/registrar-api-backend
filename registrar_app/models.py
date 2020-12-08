from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")


class Course(models.Model):
    course_name = models.CharField(max_length=255)
    students = models.ManyToManyField(
        Student, 
        through="Enrollment",
        through_field=('course', 'student')
    )

    def __str__(self):
        return(self.course_name)

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
