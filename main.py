class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_course.append(course_name)   
    
    def rate_lect(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in lecture.courses_attached and course in self.courses_in_progress and (1 <= grade <= 10):
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка' 
        
 
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

class Reviewer (Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and (1 <= grade <= 10):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        pass
 
st_ruoy = Student('Ruoy', 'Eman', 'm')
st_ruoy.courses_in_progress += ['Python']
st_ruoy.courses_in_progress += ['C++']

st_anna = Student('Anna', 'Ivanova', 'w')
st_anna.courses_in_progress += ['Python']
st_anna.courses_in_progress += ['Java']

lect_some = Lecturer('Some', 'Buddy')
lect_some.courses_attached += ['Python']
lect_some.courses_attached += ['C++']
lect_some.courses_attached += ['1C']

lect_vasilii = Lecturer('Vasilii', 'Petrov')
lect_vasilii.courses_attached += ['Python']
lect_vasilii.courses_attached += ['C++']
lect_vasilii.courses_attached += ['Java']

st_ruoy.rate_lect (lect_some, 'Python', 4)
st_ruoy.rate_lect (lect_vasilii, 'Python', 4)
st_ruoy.rate_lect (lect_some, 'Python', 14) # большая оценка
st_ruoy.rate_lect (lect_some, 'C++', 4)
st_ruoy.rate_lect (lect_vasilii, 'Java', 4) # у Ruoy нет Java

st_anna.rate_lect (lect_some, 'Python', 8)
st_anna.rate_lect (lect_vasilii, 'Python', 8)
st_anna.rate_lect (lect_vasilii, 'Python', 11) # большая оценка
st_anna.rate_lect (lect_vasilii, 'C++', 8)
st_anna.rate_lect (lect_some, 'Java', 8) # у Some нет Java
st_anna.rate_lect (lect_vasilii, 'Java', 8)

# print(lect_some.grades)
# print(lect_vasilii.grades)


rev_garry = Reviewer('Garry', 'Potter')
rev_garry.courses_attached += ['Python']
rev_garry.courses_attached += ['C++']
rev_garry.courses_attached += ['1C']




rev_garry.rate_hw(st_ruoy, 'Python', 10)
rev_garry.rate_hw(st_anna, 'Python', 6)
rev_garry.rate_hw(st_ruoy, 'Python', -5)# маленькая оценка
rev_garry.rate_hw(st_ruoy, 'C++', 10)
rev_garry.rate_hw(st_ruoy, 'Java', 10) # у Ruoy нет Java
rev_garry.rate_hw(st_anna, 'Java', 10) # у Garry нет Java




# print(st_ruoy.grades)
# print(st_anna.grades)

