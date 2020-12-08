from builtins import object

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
                'birthdate': student.birthdate,
                'email': student.email
            }
            output['students'].append(student_info)
        return output

    @property
    def student_detail(self):
        return {
            'first_name': self.info.first_name,
            'last_name': self.info.last_name,
            'birthdate': self.info.birthdate,
            'email': self.info.email
        }

