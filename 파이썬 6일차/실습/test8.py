class BookReader:
    name = str()
    def read_book(self):
        print(self.name + 'is reading Book!!')

reader = BookReader()
print(type(reader))
reader.name = 'Chris'
reader.read_book()


class BookReader:
    def __init__(self, name):
        self.name = name
    def read_book(self):
        print(self.name + 'is reading Book!!')

reader = BookReader('Chris')
reader.read_book()


class BookReader:
    country = 'South Korea'

    def __init__(self, name):
        self.name = name

    def read_book(self):
        print(self.name + ' is reading Book!!')

reader1 = BookReader('Tom')
print(reader1.country)
reader1.read_book()

reader2 = BookReader('Anna')
print(reader2.country)
reader2.read_book()


class Car:
    def drive(self):
        self.speed = 10

myCar = Car()
myCar.color = "blue"
myCar.model = "E-Class"

myCar.drive()
print(myCar.speed)

class Car:
    def drive(self):
        self.speed = 60


myCar = Car()
myCar.speed = 0
myCar.model = "E-Class"
myCar.color = "blue"
myCar.year = "2017"

print("자동차 객체를 생성하였습니다.")
print("자동차의 속도는", myCar.speed)
print("자동차의 색상은", myCar.color)
print("자동차의 모델은", myCar.model)
print("자동차를 주행합니다.")

myCar.drive()
print("자동차의 속도는", myCar.speed)

print()

class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model

    def drive(self):
        self.speed = 60

myCar = Car(0, "blue", "E-class")

print("자동차 객체를 생성하였습니다.")
print("자동차의 속도는", myCar.speed)
print("자동차의 색상은", myCar.color)
print("자동차의 모델은", myCar.model)
print("자동차를 주행합니다.")

myCar.drive()
print("자동차의 속도는", myCar.speed)

print()

class block_factory:
    def __init__(self, company):
        self.company = company

newblock = block_factory("Gole")
newblock.color = "blue"
newblock.shape = "long"

print("블록 정보 출력")
print("제조 회사 :", newblock.company)
print("블록 컬러 :", newblock.color)
print("블록 모양 :", newblock.shape)

print()

class block_factory:
    def __init__(self, company, color, shape):
        self.company = company
        self.color = color
        self.shape = shape

newblock = block_factory("Gole", "blue", "long")
newblock2 = block_factory("Gole", "black", "short")
newblock3 = block_factory("oxfold", "red", "big")

print("블록 정보 출력")
print("제조 회사 :", newblock.company, "블록 컬러 :", newblock.color, "블록 모양 :", newblock.shape)
print("제조 회사 :", newblock2.company, "블록 컬러 :", newblock2.color, "블록 모양 :", newblock2.shape)
print("제조 회사 :", newblock3.company, "블록 컬러 :", newblock3.color, "블록 모양 :", newblock3.shape)

print()

class block_factory:
    def __init__(self, company, color, shape):
        self.company = company
        self.color = color
        self.shape = shape

    def make_pink(self):
        self.color = "pink"

newblock = block_factory("Gole", "blue", "long")
print("블록 정보 출력")
print("제조회사 :", newblock.company, "블록컬러 :", newblock.color, "블록 모양 :", newblock.shape)

newblock.make_pink()

print("블록 정보 재 출력")
print("제조회사 :", newblock.company, "블록 컬러 :", newblock.color, "블록 모양 :", newblock.shape)

print()

class block_factory:
    def __init__(self, company, color, shape):
        self.company = company
        self.color = color
        self.shape = shape

    def make_pink(self):
        self.color ="pink"

    def make_short(self):
        self.shape = "short"

newblock = block_factory("Gole", "blue", "long")

print("블록 정보 출력")
print("제조회사 :", newblock.company, "블록컬러 :", newblock.color, "블록 모양 :", newblock.shape)

newblock.make_pink()
newblock.make_short()
print("블록 정보 출력")
print("제조회사 :", newblock.company, "블록컬러 :", newblock.color, "블록 모양 :", newblock.shape)

print()

class Calculator:
    def plus(self, x, y):
        return x + y
    def minus(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        return x / y

calc = Calculator()
print(calc.plus(10, 5))
print(calc.minus(10, 5))
print(calc.multiply(10, 5))
print(calc.divide(10, 5))

print()

class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model

    def __str__(self):
        msg = "속도 : " + str(self.speed) + " 색상 : " + self.color + " 모델 : " + self.model
        return msg

myCar = Car(0, "blue", "E-Class")
print(myCar)

print()

class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model

    def drive(self):
        self.speed = 60

dadCar = Car(0, "silver", "A6")
momCar = Car(0, "white", "520d")
myCar = Car(0, "blue", "E-class")

print("아빠차 스피드 :", dadCar.speed, "아빠차 컬러 :", dadCar.color, "아빠차 모델 :", dadCar.model)
print("엄마차 스피드 :", momCar.speed, "엄마차 컬러 :", momCar.color, "엄마차 모델 :", momCar.model)
print("나의차 스피드 :", myCar.speed, "나의차 컬러 :", myCar.color, "나의차 모델 :", myCar.model)

print()

class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model

    def drive(self):
        self.speed = 60

myCar = Car(0, "blue", "E-class")
yourCar = Car(0, "white", "S-class")

print(myCar.speed, yourCar.speed)

myCar.drive()
yourCar.drive()
print(myCar.speed, yourCar.speed)

print()

class Car:
    color = ""
    speed = 0
    count = 0

    def __init__(self):
        self.speed = 0
        Car.count += 1

myCar1 = Car()
myCar1.speed  = 30
print("자동차1의 현재속도 : %dkm, 생산된 자동차는 총 %d대 입니다." %(myCar1.speed, Car.count))

myCar2 = Car()
myCar2.speed = 60
print("자동차2의 현재속도 : %dkm, 생산된 자동차는 총 %d대 입니다." %(myCar2.speed, Car.count))

print()

class Car:
    def __init__(self):
        self.speed = 0

    def up_Speed(self, value):
        self.speed += value

        print(f'현재속도(수퍼클래스) : {self.speed}')


class sedan(Car):
    def up_Speed(self, value):
        self.speed += value

        if self.speed >= 150:
            self.speed = 150

        print(f'현재속도(서브클래스) : {self.speed}')


class Truck(Car):
    pass


class Sonata(sedan):
    pass


truck = Truck()
sedan = sedan()
sonata = Sonata()

print("트럭 --> ", end="")
truck.up_Speed(200)

print("승용차 --> ", end="")
sedan.up_Speed(150)

print("소나타 --> ", end="")
sedan.up_Speed(200)

print()


class Korea:
    def say(self):
        print("I'm from korea")


class South_Korea(Korea):
    pass


a = Korea()
b = South_Korea()

print(a.say())
print(b.say())