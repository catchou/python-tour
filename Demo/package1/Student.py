class Student():
    name=''
    age=0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def printStu(cls):
        print('name:' + cls.name)
        print('age:' + str(cls.age))

student = Student('鸡小萌',18)
student.printStu()
