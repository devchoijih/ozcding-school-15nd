## 클래스를 선언(만들다)입니다.

## class 클래스 이름:
## 생성자
## def __init__(self, 추가적인 매개변수):

"""
class CreateOzStuduent:
    def __init__(self, name, python, database, django, AWS):
        self.name = name,
        self.python = python,
        self.database = database,
        self.Django = django,
        self.AWS = AWS

oz_students = [
    CreateOzStuduent("백현우", 4, 3, 3, 2),
    CreateOzStuduent("홍혜인", 4, 5, 2, 4),
    CreateOzStuduent("윤은성", 3, 4, 4, 1),
    CreateOzStuduent("홍수철", 2, 3, 1, 5)
]

print(oz_students[0].name)

"""

"""
class 클래스 이름:
    def 메소드 이름(self, 추가적인 매개변수)
        pass
"""

"""
class CreateOzStuduent:
    def __init__(self, name, python, database, django, AWS):
        self.name = name
        self.python = python
        self.database = database
        self.Django = django
        self.AWS = AWS

    def get_sum(self):
        return self.python + self.database + self.Django + self.AWS
    
    def get_average(self):
        return self.get_sum() / 4
    
    def to_string(self):
        return f'{self.name}\t{self.get_sum()}\t{self.get_average()}'

oz_students = [
    CreateOzStuduent("백현우", 4, 3, 3, 2),
    CreateOzStuduent("홍혜인", 4, 5, 2, 4),
    CreateOzStuduent("윤은성", 3, 4, 4, 1),
    CreateOzStuduent("홍수철", 2, 3, 1, 5)
]

print("이름", "총점", "평균", sep='\t')
for student in oz_students:
    print(student.to_string())

"""

## isinstance() : 첫번째 매개변수에서 인스턴스(객체), 두 번째 매개션수에는
## 클래스를 입력해주면 두번째 매개변수로 입력한 클래스 키반으로 인스턴스가 생성되었는지
## True, False로 반환해줌

class Student:
    def __init__(self):
        pass

student = Student()

print("isinstance(student, Student):", isinstance(student, Student))

## __str__ 함수 선언!!!!!
"""
class CreateOzStuduent:
    def __init__(self, name, python, database, django, AWS):
        self.name = name
        self.python = python
        self.database = database
        self.Django = django
        self.AWS = AWS

    def get_sum(self):
        return self.python + self.database + self.Django + self.AWS
    
    def get_average(self):
        return self.get_sum() / 4
    
    def __str__(self):
        return f'{self.name}\t{self.get_sum()}\t{self.get_average()}'

oz_students = [
    CreateOzStuduent("백현우", 4, 3, 3, 2),
    CreateOzStuduent("홍혜인", 4, 5, 2, 4),
    CreateOzStuduent("윤은성", 3, 4, 4, 1),
    CreateOzStuduent("홍수철", 2, 3, 1, 5)
]

print("이름", "총점", "평균", sep='\t')
for student in oz_students:
    print(str(student))

"""

### 클래스 변수 ans 클래스 함수
"""
클래스 변수는 

count = 0 클래스 안에 선언후

CreateOzStuduent.count로 가져오면됨

클래스 함수는

class 클래스 이름:
    @classmethod
    def 클래스 함수명(cls, 매개변수):
        pass
        
클래스 이름.함수 이름(매개변수)

"""

class CreateOzStuduent:

    student = []
    count = 0

    @classmethod
    def print(cls):
        print("수강생 데이터베이스 정보")
        print("이름\t총점\t평균")
        for student in cls.student:
            print(str(student))

    def __init__(self, name, python, database, django, AWS):
        self.name = name
        self.python = python
        self.database = database
        self.Django = django
        self.AWS = AWS

        CreateOzStuduent.count += 1
        print(f'{CreateOzStuduent.count}번째 수강생의 정보가 추가되었습니다.')

        CreateOzStuduent.student.append(self)

    def get_sum(self):
        return self.python + self.database + self.Django + self.AWS
    
    def get_average(self):
        return self.get_sum() / 4
    
    def __str__(self):
        return f'{self.name}\t{self.get_sum()}\t{self.get_average()}'
    
CreateOzStuduent("백현우", 4, 3, 3, 2)
CreateOzStuduent("홍혜인", 4, 5, 2, 4)
CreateOzStuduent("윤은성", 3, 4, 4, 1)
CreateOzStuduent("홍수철", 2, 3, 1, 5)

print(f'현재 데이터가 입력된 총 수강생은 {CreateOzStuduent.count}입니다.')
CreateOzStuduent.print()

##프라이빗 변수
"""
변수 앞에 __만 추가하면됨
"""

##상속 과 다중상속

class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init()__ 메소드가 호출되었습니다.")
    def test(self):
        print("Parent 클래스의 test() 메소드입니다.")

class Child(Parent):
    def __init(self):
        super().__init__()
        print("Child 클래스의 __init()__ 메소드가 호출되었습니다.")

child = Child()

child.test()
print(child.value)