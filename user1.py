class Users:
    def __init__(self, type, name, pass_id, email, dob, gender, nationality, phone):
        self.set_type(type)
        self.set_name(name)
        self.set_pass_id(pass_id)
        self.set_email(email)
        self.set_dob(dob)
        self.set_gender(gender)
        self.set_nationality(nationality)
        self.set_phone(phone)

    def set_type(self, type):
        self.__type = type
    def get_type(self):
        return self.__type

    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name

    def set_pass_id(self, pass_id):
        self.__pass_id = pass_id
    def get_pass_id(self):
        return self.__pass_id

    def set_email(self, email):
        self.__email = email
    def get_email(self):
        return self.__email

    def set_dob(self, dob):
        self.__dob = dob
    def get_dob(self):
        return self.__dob

    def set_gender(self, gender):
        self.__gender = gender
    def get_gender(self):
        return self.__gender

    def set_nationality(self, nationality):
        self.__nationality = nationality
    def get_nationality(self):
        return self.__nationality

    def set_phone(self, phone):
        self.__phone = phone
    def get_phone(self):
        return self.__phone


class Faculty(Users):
    def __init__(self, type, name, pass_id, email, dob, gender, nationality, phone, course, occupation, course_hours,
                 salary, title):
        Users.__init__(self, type, name, pass_id, email, dob, gender, nationality, phone)

class Course:
    def __init__(self, course):
        course_list = []
        with open("course.txt", 'r') as file:
            course_str = file.readlines()
            course_list = str(course_str).split()
        if course in course_list:
            self.__course = course
        else:
            raise ValueError('course not found')

    def get_course(self):
        return self.__course

    def set_occupation(self, occupation):
        self.__occupation = occupation

    def get_occupation(self):
        return self.__occupation

    def set_course_hours(self, course_hours):
        if 2 <= course_hours < 18:
            self.__hours = course_hours
            self.__salary = course_hours * self.__salary
        elif 18 <= course_hours < 24:
            self.__course_hours = course_hours

    def get_course_hours(self):
        return self.__course_hours

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title


course = Course('logic')
print(course.get_course())




class TeachingAssistant(Faculty):
    def __init__(self):
