'''
num1 = 5
num2 = 3

a = (num1 > num2)
print(num1, '>', num2, ':', a)

a = (num1 < num2)
print(num1, '<', num2, ':', a)

a = (num1 >= num2)
print(num1, '>=', num2, ':', a)

a = (num1 <= num2)
print(num1, '<=', num2, ':', a)

a = (num1 == num2)
print(num1, '==', num2, ':', a)

a = (num1 != num2)
print(num1, '!=', num2, ':', a)

print()

n = 7 - 4

result = (n==3)
print("n==3 :", result)

result = (n==5)
print("n==5 :", result)

print()

score = int(input("성적을 입력하시오 : "))
if score >=60:
    print("합격입니다.")
else:
    print("불합격입니다.")

print()

number = int(input("정수를 입력하세요. : "))

if number > 0:
    print("양수 입니다.")
else:
    print("음수 입니다.")

number = int(input("정수를 입력하세요. : "))

if number < 0:
    number = -number

print("절대값은 %d입니다." % number)

print()

num = int(input("정수를 입력하시오: "))
if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

print()

num = int(input("정수를 입력하시오 : "))
if num % 2 == 1:
    print("홀수입니다.")
else:
    print("짝수입니다.")

print()

myAge = int(input("당신의 나이는 몇 살 인가요?"))
if myAge > 15:
    print("이 영화를 볼수 있는 나이입니다.")
else:
    print("이 영화를 볼 수 없습니다.")

print()

import random

print("동전 던지기 게임을 시작합니다.")

coin = random.randrange(2)

if coin == 0:
    print("앞면입니다.")
else:
    print("뒷면입니다.")
print("게임이 종료되었습니다.")


print()

import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

answer = int(input("다음 " + str(number1) + " + " + str(number2) + " 두 수의 합은 얼마인가? "))

print(number1, "+", number2, "=", answer, "는", (number1 + number2 == answer))

print()

import random

time = random.randint(1, 24)
print("좋은 아침입니다. 지금 시각은 " + str(time) + "시 입니다.")

sunny = random.choice([True, False])

if sunny:
    print("현재 날씨가 화창합니다.")
else:
    print( "현재 날씨가 화창하지 않습니다.")
if (6 <= time < 9) and sunny:
    print("종달새가 노래를 한다.")
else:
    print("종달새가 노래를 하지 않는다.")
    
print()

import random

options=["왼쪽", "중앙", "오른쪽"]
computer_choice = random.choice(options)
user_choice = input("어디를 수비하시겠어요?(왼쪽, 중앙, 오른쪽): ")

if computer_choice == user_choice:
    print(computer_choice + " : " + user_choice)
    print("수비에 성공하셨습니다.")
else:
    print(computer_choice + " : " + user_choice)
    print("페널티 킥이 성공하셨습니다.")

print()

import random

print("임의의 정수 생성 범위를 지정 하시오")
start_num = int(input("정수의 시작범위 : "))
end_num = int(input("정수의 시작범위 : "))
random_number = random.randint(start_num, end_num)
print("생성된 숫자는 %d입니다." %random_number)

print()

a = 100; b = 100
print("a is b : ", a is b, " a==b : ", a==b)

a = 300; b = int(3000/10)
print("a is b : ", a is b, " a==b : ", a==b)

print()

a = 8; b = 5
result = (a==8 and b==4)
print("a==8 and b==4 :", result)

result = (a > 7 or b > 7)
print("a > 7 or b > 7 :", result)

print()

score = int(input("점수를 입력하세요:"))
if score >= 90:
    grade = 'A'
if score >= 80:
    grade = 'B'
if score >= 70:
    grade = 'C'
if score >= 60:
    grade ='D'
if score < 60:
    grade ='F'
print(grade)

print()

score = int(input("점수를 입력하세요: "))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade ='D'
else:
    grade ='F'
print(grade)

print()

age = int(input("당신의 나이를 입력하세요. "))

if age >= 10:
    if age < 20:
        print('student')
    else:
        print('adult')
else:
    print('kid')
    
print()

age = int(input('당신의 나이를 입력하세요. '))

if age >= 20:
    print('adult')
elif age >= 10:
    print('student')
else:
    print('kid')

print()

num1 = int(input('num1 입력 : '))
num2 = int(input('num2 입력 : '))

if num1 * num2 > 0:
    print(str(num1) + " * " + str(num2) + " = " + str(num1 * num2) + "(양수)")
elif num1 * num2 < 0:
    print(str(num1) + " * " + str(num2) + " = " + str(num1 * num2) + "(음수)")
    
print()

num = int(input("총점을 입력하세요 : "))

if num >= 90:
    print("학점은 A 입니다.")
elif num >= 80:
    print("학점은 B 입니다.")
elif num >= 70:
    print("학점은 C 입니다.")
else:
    print("학점은 D 입니다.")
    
print()

num1 = int(input("영어점수 입력 : "))
num2 = int(input("수학점수 입력 : "))

if(num1 + num2 > 110):

    if(num1 < 40):
        print("불합격 : 영어 점수가 부족합니다.")
    elif(num2 < 40):
        print("불합격 : 수학 점수가 부족합니다.")

print("총점 : %d점" %(num1 + num2))

print()

num = int(input("손가락 둘레를 입력하세요(mm) : "))

if 51.0 < num <= 52.0:
    print("9호를 추천합니다.")
elif 52.0 < num <= 53.0:
    print("10호를 추천합니다.")
elif 53.0 < num <= 54.0:
    print("11호를 추천합니다.")
elif 54.0 < num <= 55.0:
    print("12호를 추천합니다.")
else:
    print("반지 제작이 불가능 합니다.")
    
print()

print("1.덧셈 2.뺼셈 3.곱셈 4.나눗셈")
num = int(input("어떤 연산을 원하는지 번호를 입력하세요 : "))
if 1 <= num <= 4:
    print("연산을 원하는 숫자 두개를 입력하세요(양의 정수만 가능)")
    num1 = int(input())
    num2 = int(input())

    if num == 1:
        #d = num1+num2
        print(num1, " + ", num2, " = ",  num1 + num2)
    elif num == 2:
        print(num1, " - ", num2, " = ", num1 - num2)
    elif num == 3:
        print(num1, " * ", num2, " = ", num1 * num2)
    elif num == 4:
        print(num1, " / ", num2, " = ", num1 / num2)

else:
    print("잘못 입력하였습니다.")

print()

count = 0
while count < 2:
    print(count)
    count = count + 1

print()

count = 0
while count < 2:
    print("프로그램은 재밌습니다.!")
    count = count + 1

print()

i = 0
while i < 5:
    print(i)
    i = i + 1

print()

i = 1
while i <= 5:
    print(i, "번째 반복")
    i = i + 1

print()

while True:
    print("반복출력")

print()

i = 1
while i <= 100:
    print(i)
    i = i + 2

print()

i = 1
while i <=30:
    print(i, "% 4 =", i%4)
    i = i + 1
    
print()

while(True):
    n = int(input("정수를 입력하세요('0' 입려시 종료) "))
    if n == 0:
        print('EXIT')
        break
    elif n % 2 == 0:
        print(n, 'is even number')
    else:
        print(n, 'is odd number')
        
print()

i = 0; j = 1; fibo = 0

while fibo < 100:
    fibo = i + j
    print(fibo, end = " ")
    i = j
    j = fibo

print()

name = ""
while name != 'q':
    name = input("당신의 이름을 입력하세요. 'q'를 입려하면 종료 됩니다. : ")
    print(name)
    
print()

answer = 50; number = 0

while number != 50:
    number = int(input("예상 숫자를 입력하세요 : "))
    if answer == number:
        print("정답")
    elif answer > number:
        print("UP")
    else:
        print("DOWN")

print()

from random import *
throw = 0

print("주사위 프로그램을 시작합니다. 첫번째 숫자는 ")
while throw != 'q':
    print(randint(1, 6))
    throw = input("아무거나 누르면 주사위가 던져집니다. 종료를 원하시면 'q'를 입력해주세요.")
    
print()

num = 0;

while num != 1:
    num = int(input("(종료 '1') 구구단 몇 단을 출력할까요 : "))
    i = 1

    while i < 10:
        print(num, "x", i, "=", num * i)
        i = i + 1 

print()

num = 0
num = int(input("(종료 '1') 숫자 입력 : "))

while num != 1:
    i = 1
    sum_n = 0

    while i < num + 1:
        sum_n = sum_n + i
        i = i + 1
    print(sum_n)
    num = int(input("(종료 '1')숫자 입력 : "))

print()

hp = 100

while hp > 0:
    print("주인공의 체력은", hp, "입니다.")
    damage = int(input("얼마의 데미지를 입히시겠습니까 : "))
    hp = hp - damage

print("주인공이 죽었습니다.")

print()

i = 1; j =0
meal = ['아침', '점심', '저녁', '야식']

while i > 0:
    i = int(input("(종료 '0')며칠이 지났습니까 : "))
    j = i

    while j > 0:
        for k in meal:
            print(k)
        j = j - 1
        
print()

for i in range(5):
    print(i, end=" ")

print()

for i in range(1, 5):
    print(i, end=" ")

print()

for i in range(1, 10, 2):
    print(i, end=" ")
    
print()

array = [273, 32, 103, 57, 52]

for i in array:
    print(i)

print()

for element in array:
    print(element)
    
print()

array = [273, 32, 103, 57, 52]

for i in array:
    print(i)

print()

for i in range(len(array)):
    print(array[i])

print()

for i in reversed(range(10)):
    print("{}번째 반복".format(i))

print()

for i in range(11):
    print(i)

print()

for i in range(5, 16):
    print(i, end=" ")

print()

for i in range(0, 21, 2):
    print(i, end=" ")

print()

for i in range(-100, 101, 4):
    print(i, end=" ")

print()

score = [75, 83, 95, 99, 67, 55]
number = 0

print("2019 제2회 한국사 시험 결과")

for i in score:
    number = number + 1
    if i >= 70:
        print(number, "번 학생은 1급입니다.")
    elif i >= 60:
        print(number, "번 학생은 2급입니다.")
    else:
        print(number, "번 학생은 불합격입니다.")

print()

for i in 'abcdefg':
    print(i)

for i in ['apple', 'banana', 'melon']:
    print(i)

print()

for i in range(1, 10, 2):
    print(i)

print()

for i in range(10, 0, -1):
    print(i)
    
print()

a = 0; b =1
for i in range(20):
    print(a, end=" ")
    n = a + b
    a =  b
    b = n

print()

a = int(input("홀수는 1, 짝수는 2를 입력해주세요 : "))

for i in range(a, 101, 2):
    print(i)

print()

for i in range(10):
    if i == 5:
        break
    print(i)

print("END of Program")

print()

sum = 0
number = 0

while number < 20:
    number += 1
    sum += number
    if sum >= 100:
        break

print("마지막 숫자는", number, "입니다.")
print("합계는", sum, "입니다.")

print()

for i in range(0, 3, 1):
    for k in range(0, 2, 1):
        print("파이썬은 꿀잼입니다. ^^(i값 : %d, k값 : %d)" %(i, k))
        
print()

i, k = 0, 0

for i in range(2, 10, 1):
    for k in range(1, 10, 1):
        print("%d X %d = %2d" %(i, k, i * k))
    print("")

print()

i, k, guguLine = 0, 0, ""

for i in range(2, 10):
    guguLine = guguLine + ("# %d단 #" % i)

print(guguLine)

for i in range(1, 10):
    guguLine = ""
    for k in range(2, 10):
        guguLine = guguLine + str("%2dX%1d=%-2d" % (k, i, k * i))

    print(guguLine)

print()

user_input = int(input("구구단 몇 단을 계산할까? "))
if (2 <= user_input <= 9):
    print("구구단", user_input, "단을 계산한다.")

    for i in range(1, 10):
        result = user_input * i;
        print(user_input, "x", i, "=", result)

print()

sentense = "I Love You"
reverse_sentense = ''

for char in sentense:
    reverse_sentense = char + reverse_sentense

print(reverse_sentense)

print()

import random

guess_number = random.randint(1, 100)
user_input = int(input("숫자를 맞춰보세요.(1~100)"))

while user_input != guess_number:
    if user_input > guess_number:
        print("입력한 숫자가 더 큽니다.")
    else:
        print("입력한 숫자가 더 작습니다.")

    user_input = int(input())

print("정답입니다. 정받은", user_input, "입니다.")

print()

num = int(input("enter the number : "))

sum = 0

for i in range(1, num + 1, 1):
    sum += i

print("총합 : %d" %sum)

print()

num = int(input("enter the number : "))
step = 0
sum = 0

while (step <= num):
    sum += step
    step += 1

print(sum)

'''

print()

num = int(input("enter the number : "))
sum = 0

while (True):
    if num == 0:
        print("종료")
        break
    for i in range(1, num + 1, 1):
        sum += i

    print("총합 : %d" %sum)
    sum = 0
    num = int(input("enter the number : "))

