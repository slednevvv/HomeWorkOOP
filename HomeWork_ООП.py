class Student:
  students_list = []
  
  def __init__(self, name, surname, gender, grade_med = 0):
    self.name = name
    self.surname = surname
    self.gender = gender
    self.finished_courses = []
    self.courses_in_progress = []
    self.grades = {}
    self.list_med_grede = []
    self.grade_med = grade_med
    self.students_list.append(self)
    
  def rate_mentor(self, lecturer, course, grade):
    if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
      if course in lecturer.grades:
        lecturer.grades[course] += [grade]
      else:
        lecturer.grades[course] = [grade]
    else:
      return 'Ошибка'

  def medium_grade_student(self):
    for key, vol in self.grades.items():
      vol_grades = vol
      aver_grades = sum(vol_grades)/len(vol_grades)
      self.grade_med = aver_grades
      self.list_med_grede.append(aver_grades)      

  def __str__(self):
    student_name_surname = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задание: {self.grade_med}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"
    return student_name_surname

  def __lt__(self, other):
    if not isinstance(other, Student):
      print('Not a Student!')
      return
    return self.list_med_grede < other.list_med_grede

class Student:
  students_list = []
  
  def __init__(self, name, surname, gender, grade_med = 0):
    self.name = name
    self.surname = surname
    self.gender = gender
    self.finished_courses = []
    self.courses_in_progress = []
    self.grades = {}
    self.list_med_grede = []
    self.grade_med = grade_med
    self.students_list.append(self)
    
  def rate_mentor(self, lecturer, course, grade):
    if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
      if course in lecturer.grades:
        lecturer.grades[course] += [grade]
      else:
        lecturer.grades[course] = [grade]
    else:
      return 'Ошибка'

  def medium_grade_student(self):
    for key, vol in self.grades.items():
      vol_grades = vol
      aver_grades = sum(vol_grades)/len(vol_grades)
      self.grade_med = aver_grades
      self.list_med_grede.append(aver_grades)      

  def __str__(self):
    student_name_surname = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задание: {self.grade_med}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"
    return student_name_surname

  def __lt__(self, other):
    if not isinstance(other, Student):
      print('Not a Student!')
      return
    return self.list_med_grede < other.list_med_grede


class Mentor:
  def __init__(self, name, surname):
      self.name = name
      self.surname = surname
      self.courses_attached = []
        

class Lecturer(Mentor):
  lecturer_list = []
  
  def __init__(self, name, surname, grade_med = 0):
    super().__init__(name, surname)
    self.grades = {}
    self.list_med_grede = []
    self.grade_med = grade_med
    self.lecturer_list.append(self)

  def medium_grade_lecturer(self):
    for key, vol in self.grades.items():
      vol_grades = vol
      aver_grades = sum(vol_grades)/len(vol_grades)
      self.grade_med = aver_grades
      self.list_med_grede.append(aver_grades)
      
  def __str__(self):
    lecturer_name_surname = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.grade_med}'
    return lecturer_name_surname

  def __lt__(self, other):
    if not isinstance(other, Lecturer):
      print('Not a Lecturer!')
      return
    return self.list_med_grede < other.list_med_grede  
        

class Reviewer(Mentor):
  def rate_hw(self, student, course, grade):
      if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
          if course in student.grades:
              student.grades[course] += [grade]
          else:
              student.grades[course] = [grade]
      else:
          return 'Ошибка'

  def __str__(self):
    reviewer_name_surname = f'Имя: {self.name}\nФамилия: {self.surname}'
    return reviewer_name_surname     


student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Max', 'Payne', 'your_gender')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['Введение в программирование']

mentor_1 = Reviewer('Some', 'Buddy')
mentor_1.courses_attached += ['Python', 'Git']

mentor_2 = Reviewer('Joe', 'Rogan')
mentor_2.courses_attached += ['Python', 'Git']

lecturer_1 = Lecturer('Some', 'Buddy')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Mickael', 'DeSanta')
lecturer_2.courses_attached += ['Python']

mentor_1.rate_hw(student_1, 'Python', 9)
mentor_1.rate_hw(student_1, 'Python', 9)
mentor_1.rate_hw(student_1, 'Python', 9)

mentor_1.rate_hw(student_1, 'Git', 8)
mentor_1.rate_hw(student_1, 'Git', 8)
mentor_1.rate_hw(student_1, 'Git', 8)

mentor_1.rate_hw(student_2, 'Python', 7)
mentor_1.rate_hw(student_2, 'Python', 7)
mentor_1.rate_hw(student_2, 'Python', 7)

mentor_1.rate_hw(student_2, 'Git', 6)
mentor_1.rate_hw(student_2, 'Git', 6)
mentor_1.rate_hw(student_2, 'Git', 6)

student_1.rate_mentor(lecturer_1, 'Python', 8)
student_1.rate_mentor(lecturer_1, 'Python', 7)
student_1.rate_mentor(lecturer_1, 'Python', 9)

student_1.rate_mentor(lecturer_2, 'Python', 5)
student_1.rate_mentor(lecturer_2, 'Python', 5)
student_1.rate_mentor(lecturer_2, 'Python', 5)

student_2.rate_mentor(lecturer_1, 'Python', 4)
student_2.rate_mentor(lecturer_1, 'Python', 4)
student_2.rate_mentor(lecturer_1, 'Python', 4)

student_2.rate_mentor(lecturer_2, 'Python', 4)
student_2.rate_mentor(lecturer_2, 'Python', 4)
student_2.rate_mentor(lecturer_2, 'Python', 4)

lecturer_1.medium_grade_lecturer()
lecturer_2.medium_grade_lecturer()

student_1.medium_grade_student()
student_2.medium_grade_student()

print('Оценка Student')
print('Оценка  Ruoy Eman за ДЗ', student_1.grades)
print('Оценка Max Payne за ДЗ', student_2.grades)
print()
print('Оценка Lecturer')
print('Оценка Some Buddy за лекцию', lecturer_1.grades)
print('Оценка Mickael DeSanta за лекцию', lecturer_2.grades)
print()
print('Пепегрузка __str__ для  Reviewer')
print(mentor_1)
print(mentor_2)
print()
print('Перегрузка __str__ для Lecturer')
print(lecturer_1)
print(lecturer_2)
print()
print('Перегрузка __str__  для Student')
print(student_1)
print(student_2)
print()
print('Сравнение студентов')
print(student_1 < student_2)
print()
print ('Сравнение преподователей')
print(lecturer_1 < lecturer_2)
print()

def average_grade_course_student(students_list, Python):
  total_points = 0
  number_of_grades = 0
  for student in students_list:
    if Python in student.courses_in_progress:
        student_course_medium = sum(student.grades[Python]) / len(student.grades[Python])
        total_points += student_course_medium
        number_of_grades += 1
  if number_of_grades == 0:
    print('Нет студентов изучающих этот курс')
  else:
    print(f'Средний балл для студнетов по курсу Python: {total_points / number_of_grades}')

    
average_grade_course_student(Student.students_list, 'Python')

 
def average_grade_course_lecturer(lecturer_list, Python):
  total_points = 0
  number_of_grades = 0
  for lecturer in lecturer_list:
    if Python in lecturer.courses_attached:
        lecturer_course_medium = sum(lecturer.grades[Python]) / len(lecturer.grades[Python])
        total_points += lecturer_course_medium
        number_of_grades += 1
  if number_of_grades == 0:
    print('Нет лекторов преподающих этот курс')
  else:
    print(f'Средний балл для лекторов по курсу Python: {total_points / number_of_grades}')

    
average_grade_course_lecturer(Lecturer.lecturer_list, 'Python')
