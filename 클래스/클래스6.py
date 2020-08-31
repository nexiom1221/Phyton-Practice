class Student:
    count = 0
    students = []

    @classmethod
    def print(cls):
        print("--------학생 목록--------")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("-------------------------")
    
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)
    
    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    
    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}\t".format(self.name, self.get_sum(), self.get_average())
    
Student("윤인성", 78, 87, 85, 95)
Student("연하진", 68, 27, 35, 55)
Student("구지연", 78, 87, 85, 15)
Student("나선주", 78, 17, 25, 75)
Student("윤인성", 78, 27, 35, 85)

Student.print()
