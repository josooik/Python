'''
def calulate_rectangle_area(x,y):
    return x*y
area = calulate_rectangle_area(5, 4)

print(area)

rectangle_x = 10
rectangle_y = 20

print("사각형 x의 길이 : ", rectangle_x)
print("사각형 y의 길이 : ", rectangle_y)

area = calulate_rectangle_area(rectangle_x, rectangle_y)
print("사각형의 넓이 : ", area)

print()

def add():
    value1 = 2
    value2 = 3
    print("value1 + value2 = ", value1 + value2)

add()

print()

def add():
    value1 = 2
    value2 = 3
    return  value1 + value2

sum = add()
print(sum)

print()

# 매개변수 x 반환값 x
def rectangle_area():
    print(5*7)

rectangle_area()

# 매개변수 O 반환값 X
def retangle_area1(x,y):
    print(x*y)

retangle_area1(5,7)

# 매개변수 X 반환값 O
def retangle_area2():
    return 5*7

print(retangle_area2())

# 매개변수 O 반환값 O
def retangle_area3(x,y):
    return x*y

print(retangle_area3(5,7))

print()

def sub_number(number1, number2):
    result = number1 - number2
    return result

number1 = int(input("첫번째 숫자를 입력하세요 : "))
number2 = int(input("두번째 숫자를 입력하세요 : "))
diff_number = sub_number(number1, number2)
print("두수의 차이는", diff_number, "입니다.")

print()

def sub_number(number1, number2):
    result = number1 - number2
    print("두수의 차이는", result, "입니다.")

number1 = int(input("첫번째 숫자를 입력하세요 : "))
number2 = int(input("두번째 숫자를 입력하세요 : "))
diff_number = sub_number(number1, number2)

print()

def increase_3(number1):
    result = number1 + 3
    return result

nnumber1 = int(input("정수를 입력하세요 : "))
print(nnumber1, "보다 3 큰 수는", increase_3(nnumber1), "입니다.")

print()

def sum(num1, num2):
    result = num1 + num2
    return result

number1 = int(input("첫번째 정수를 입력하세요 : "))
number2 = int(input("두번째 정수를 입력하세요 : "))
sum_number = sum(number1, number2)
print("두수의 합은 %d + %d = %d 입니다." %(number1, number2, sum_number))

print()

def sum(num1, num2):
    result = num1 + num2
    return result

def average(num1, num2):
    result = int((num1 + num2) / 2)
    return result

n1, n2 = map(int, input("정수를 2개를 입력하세요 ").split(" "))

sum_result = sum(n1, n2)
print("두수의 합은 {} + {} = {} 입니다.".format(n1, n2, sum_result))

avg_result = average(n1, n2)
print("두수의 합은 ({} + {}) / 2 = {} 입니다.".format(n1, n2, avg_result))

print()

def cirsum(width, height):
    result = (width + height) * 2
    return result

width = int(input("사각형의 폭을 입력하세요 : "))
height = int(input("사각형으 ㅣ높이를 입력하세요 : "))
rect_round = cirsum(width, height)

print("사각형의 둘레의 길이는 (%d + %d) * 2 = %d 입니다." %(width, height, rect_round))

print()

def f():
    s = "I Love London!"
    print(s)

s = "I Love Paris!"
f()
print(s)

print()

def f():
    global s
    s = "I Loeve London!"
    print(s)

s = "I Love Paris!"
f()
print(s)

print()

def calculate(x,y):
    total = x + y
    print("In Function => total : %d" % (total))
    return total

a = 5; b = 7; total = 0
print("In Main => total : %d" %(total))
sum = calculate(a, b)
print("After Calculation => Total : %d" %(total))

print()

def print_number(a, b, c):
    print(a)
    print(b)
    print(c)

# 언패킹
# 함수(*리스트)
# 함수(*튜블)
x = [10, 20, 30]
print_number(*x)

print()

def print_something(my_name, your_name):
    print("Hello {0}, My name is {1}".format(your_name, my_name))

print_something("Gildong", "PYTHON")
print_something(your_name="PYTHON", my_name="Gildong")

print()

def print_something(my_name, your_name="PYTHON"):
    print("Hello {0}, My name is {1}".format(your_name, my_name))

print_something("Gildong", "PYTHON")
print_something(my_name="Gildong")

print()

# 가변 인수
def asterisk_test(a, b, *args):
    return a + b + sum(args)

print(asterisk_test(1, 2, 3, 4, 5))

print()

# 고정 가변 인수

def print_numbers(a, *args):
    print(a)

    for arg in args:
        print(arg)

x = [10, 20, 30]
print_numbers(*x)

print()

import math

a = 1; b = -2; c = 1
print((-b + math.sqrt(b**2 - (4*a*c))) / (2*a))
print((-b - math.sqrt(b**2 - (4*a*c))) / (2*a))

print()

import math

def get_result_quadratic_equation(a, b, c):
    values = []
    values.append((-b + math.sqrt(b**2 - (4*a*c))) / (2*a))
    values.append((-b - math.sqrt(b**2 - (4*a*c))) / (2*a))
    return values

a = 1; b = -2; c =1
print(get_result_quadratic_equation(a, b, c))

print()

def cal_area(bottom, height):
    area = float(0.5 * bottom * height)
    return area

bottom = int(input("밑변을 입력하세요 : "))
height = int(input("높이를 입력하세요 : "))
triangle_area = cal_area(bottom, height)

print("삼각형의 면적은 (%d * %d * 0.5) = %.1f" % (bottom, height, triangle_area))

print()

def change_temp(x):
    temperature = float((9 / 5) * x + 32)
    return temperature

temp = float(input("섭씨온도를 입력하세요(실수형) : "))
chtemp = change_temp(temp)
print("화씨온도는 %.1f 입니다.", chtemp)

print()


def change_meter(meter):
    feet = float(meter / 0.305)
    yard = float(meter * 1.0936)
    return (yard, feet)

meter = float(input("meter를 입력 하시오 : "))
yard, feet = change_meter(meter)
print("%.1f meter = %.2f yard\n%.1f meter = %.2f feet" %(meter, yard, meter,feet))

print()

def max_score(score_list):
    max_num = 0
    for score in score_list:
        if score > max_num:
            max_num = score

    return max_num

def min_score(score_list):
    min_num = score_list[0]
    for score in score_list:
        if score < min_num:
            min_num = score

    return min_num

def diff_score(max_value, min_value):
    diff_num = 0
    if max_value > min_value:
        diff_num = max_value - min_value
    else:
        diff_num = min_value - max_value

    return diff_num

math_score = [80, 66, 70, 83, 50, 77, 87, 92, 73, 89]
max_value = max_score(math_score)
min_value = min_score(math_score)
diff_value = diff_score(max_value, min_value)

print("max : %d\nmin : %d\ngap_score : %d" %(max_value, min_value, diff_value))

print()

for i in range(10):
    try:
        print(10 / i)
    except ZeroDivisionError:
        print("Not divided by 0")

print()

for i in range(10):
    try:
        print(10 / i)
    except ZeroDivisionError as e :
        print(e)
        print("Not divided by 0")

print()

for i in range(10):
    try:
        result = 10 / i
    except ZeroDivisionError:
        print("Not divided by 0")
    else:
        print(result)

print()

try:
    for i in range(1, 10):
        result = 10 // i
        print(result)
except ZeroDivisionError:
    print("Not divided by 0")
finally:
    print("종료되었다.")

print()

while True:
    value = input("변환할 정수값을 입력 : ")
    for digit in value:
        if digit not in "0123456789":
            raise ValueError("숫자값을 입력하지 않습니다.")
    print("정수값으로 변환된 숫자-", int(value))

print()

a = [1, 2, 3]
try:
    print(a[3])
except IndexError:
    print("없는 값을 호출하였습니다.")

print()

birth = {"홍길동":"2000년 3월 1일", "김춘추":"604년", "김유신":"595년"}
a = ""

while a != 'q':
    a = input("생일을 알고 싶은 사람을 입력하세요 : ")
    try:
        print(birth[a])
    except KeyError:
        print("데이터베이스에 존재하지 않는 이름입니다.")


print()


# 문자열 바꾸기 : str.replace(바꿀 문자, 새로 바뀔 문자)
str = "Hello World"
print(str)
print(str.replace('World', 'Python'))

'''
