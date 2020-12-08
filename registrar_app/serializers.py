from builtins import object

# students 
class StudentSerializer(object):
    def __init__(self, info):
        self.info = info

    @property
    def all_students(self):
        output = {'students': []}

        for student in self.info:
            student_info = {
                'first_name': student.first_name,
                'last_name': student.last_name,
                'age': student.age
            }
            output['students'].append(student_info)
        return output

    @property
    def student_detail(self):
        courses = []
        for course in self.body.courses:
            courses.append({'course_name': course.course_name})
        return {
            'first_name': self.info.first_name,
            'last_name': self.info.last_name,
            'age': self.info.age
            'courses': courses
        }

# courses
class CourseSerializer(object):
    def __init__(self, info):
        self.info = info

    @property
    def all_courses(self):
        output = {'courses': []}

        for course in self.info:
            course_info = {
                'course_name': course.course_name,
            }
            output['courses'].append(course_info)
        return output

    @property
    def course_detail(self):
        students = []
        for student in self.body.students:
            students.append({
                'first_name': student.first_name,
                'last_name': student.last_name,
                'age': student.age
            })
        return {
            'course_name': self.info.course_name,
            'students': students
        }

