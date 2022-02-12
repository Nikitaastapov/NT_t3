class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)   
    
    def rate_lect(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in lecture.courses_attached and course in self.courses_in_progress and (1 <= grade <= 10):
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def st_aw_grades(self):
        aw_grades_st = self.grades
        res_st = []
        for i in aw_grades_st.keys():
            for j in aw_grades_st[i]:
                res_st.append(j)
        
        return round(sum(res_st)/len(res_st),1)
   
    def __str__(self):
        name = self.name
        surname = self.surname
        aw_grade = self.st_aw_grades()
        st_cours_in_pr = ', '.join (self.courses_in_progress)
        st_cours_fin = ', '.join (self.finished_courses)
        res = f'Имя: {name}\nФамилия: {surname}\nСредняя оценка за домашние задания: {aw_grade}\nКурсы в процессе изучения:{st_cours_in_pr}\nЗавершенные курсы: {st_cours_fin}'
        return res
    
    def __gt__(self, other):
        if not isinstance(other, Student):
            print('нужно указать имя студента')
            return
        else:
            st_1 = self.st_aw_grades()
            st_2 = other.st_aw_grades()
        return st_1 > st_2
        
 
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
   
    def lec_aw_grades(self):
        aw_grades_lec = self.grades
        res_lec = []
        for i in aw_grades_lec.keys():
            for j in aw_grades_lec[i]:
                res_lec.append(j)
        
        return round(sum(res_lec)/len(res_lec),1)
    
    def __str__(self):
        name = self.name
        surname = self.surname
        aw_grade = self.lec_aw_grades()
        res = f'Имя: {name}\nФамилия: {surname}\nСредняя оценка за лекции: {aw_grade}'
        return res
    
    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('нужно указать имя лектора')
            return
        else:
            lec_1 = self.lec_aw_grades()
            lec_2 = other.lec_aw_grades()
        return lec_1 > lec_2


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
        rv_name = self.name
        rv_surname = self.surname
        res = f'Имя: {rv_name}\nФамилия: {rv_surname}'
        return res
 
    
st_ruoy = Student('Ruoy', 'Eman', 'm')
st_ruoy.courses_in_progress += ['Python']
st_ruoy.courses_in_progress += ['C++']
st_ruoy.add_courses('Математика')
st_ruoy.add_courses('Логика')

st_anna = Student('Anna', 'Ivanova', 'w')
st_anna.courses_in_progress += ['Python']
st_anna.courses_in_progress += ['Java']
st_anna.add_courses('Математика')
st_anna.add_courses('Логика')


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

rev_germ = Reviewer('Germiona', 'Granger')
rev_germ.courses_attached += ['Python']
rev_germ.courses_attached += ['C++']
rev_germ.courses_attached += ['Java']

rev_garry.rate_hw(st_ruoy, 'Python', 5)
rev_garry.rate_hw(st_anna, 'Python', 5)
rev_garry.rate_hw(st_ruoy, 'Python', -5)# маленькая оценка
rev_garry.rate_hw(st_ruoy, 'C++', 5)
rev_garry.rate_hw(st_ruoy, 'Java', 5) # у Ruoy нет Java
rev_garry.rate_hw(st_anna, 'Java', 5) # у Garry нет Java

rev_germ.rate_hw(st_ruoy, 'Python', 7)
rev_germ.rate_hw(st_anna, 'Python', 7)
rev_germ.rate_hw(st_ruoy, 'Python', 12)# большая оценка
rev_germ.rate_hw(st_ruoy, 'C++', 7)
rev_germ.rate_hw(st_ruoy, 'Java', 7) # у Ruoy нет Java
rev_germ.rate_hw(st_anna, 'Java', 7) 

# print(st_ruoy.grades)
# print(st_anna.grades)

# print(rev_garry)
# print(rev_germ)

# print(lect_some)
# print(lect_vasilii)

# print(st_ruoy)
# print(st_anna)

# print(lect_some > lect_vasilii)
# print(lect_some < lect_vasilii)
# print(lect_some < st_anna)# разные классы

# print(st_anna > st_ruoy)
# print(st_anna < st_ruoy)
# print(lect_vasilii < st_ruoy)# разные классы

students_list = [st_ruoy, st_anna]

def rate_st_on_course(students_list,course):
    aw_rate = []
    for k in students_list:
        if isinstance(k, Student):
            for l in k.grades[course]:
                aw_rate.append(l)
    return round(sum(aw_rate)/len(aw_rate),1)
        
# print(rate_st_on_course(students_list, 'Python'))

lecturer_list = [lect_some, lect_vasilii]

def rate_lec_on_course(lecturer_list,course):
    aw_rate = []
    for k in lecturer_list:
        if isinstance(k, Lecturer):
            for l in k.grades[course]:
                aw_rate.append(l)
    return round(sum(aw_rate)/len(aw_rate),1)
        
# print(lect_some.grades)
# print(lect_vasilii.grades)
# print(rate_lec_on_course(lecturer_list, 'Python'))