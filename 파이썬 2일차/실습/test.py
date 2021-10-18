'''
dist = 12
print(int(0.2467 * dist + 4.159))

print("=" * 50)
print("test")
print("=" * 50)

print(len("test"))


a, b, c = map(int, input("변수 3개를 입력하세요").split())

#a = input("1개 변수 입력")
#b = input("2개 변수 입력")
#c = input("3개 변수 입력")


print("합", a + b + c)
print("곱", a * b * c)

print(1, 2, 3, sep=',')
print(1, 2, 3, sep=', ')

print(3840,2160, sep='x')

print("당신의 나이는 %d살이고 %s에 삽니다." %(20, "대구"))
print("당신의 나이는 {}살이고 {}에 삽니다." .format(20, "대구"))


a=11
b=22

print("a : ",a, "b : ", b)

c = a
a = b
b = c

print("a : ",a, "b : ", b)

string1 = "red apple"
string2 = "yellow banana"

print(string2[:6] + string1[3:], string1[:3] + string1[:3]+string2[6:])

name = "Hong Gildong"

family_name = name[:4]
print(family_name)

name = input("이름을 입력하세요 : ")
height = int(input("키(cm)를 입력하세요 : "))
weight = int(input("몸무게(kg)를 입력하세요 : "))
bmi = weight / (height / 100)**2
print()
print(name + "님의 키는 ",  height, "cm 이고 몸무게는 ", weight, "kg 입니다.", sep='')
print("BMI 지수는", round(bmi, 2), "입니다.")


candies = ['딸기맛', '레몬맛', '수박맛', '박하맛', '우유맛']
print(type(candies))
print(candies)

list1 = list(range(3, 10))
print(list1)

a = list("python3")
print(a)

b = list(range(1, 100, 3))
print(b)

c = list(range(2, 100, 2))
print(c)

colors = ['red', 'blue', 'green']
print(colors[0])
print(colors[1])
print(colors[2])
print(len(colors))

colors = ['red', 'blue', 'green', 4, 5, 6]
print(colors[0])
print(colors[1] + str(colors[3]))
print(colors[1] * 3 + colors[2])

letters = ['A', 'B', 'C', 'D', 'E', 'F']
print(letters[:])

cities = ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']
print(cities[0:6])
print(cities[-8:])
print(cities[-50:50])
print(cities[::2])
print(cities[::-1])

a = ["apple", "banana", "cat", "dinosaur"]
print(a[1:3])
print(a[:2])
print(a[2:])

a = ["apple", "banana", [1, 2, ["@", "%"]]]
print(a[2])
print(a[2][0])
print(a[2][2][0])

colors = []
print(colors)
colors.append('red')
print(colors)
colors.append('blue')
print(colors)
colors.append('green')
print(colors)

colors =['red', 'blue', 'green']
print(colors)
colors[0] = 'orange'
print(colors)

a = ['A', 'B', 'C']
a[1] = 'b'
print(a)
a[1:2] = ['B', 'b', 'bear']
print(a)

colors = ['orange', 'blue', 'green']
print(colors)
del colors[0]
print(colors)

colors = ['orange', 'blue', 'green']
print(colors)
colors.pop()
print(colors)

colors2 = colors.pop()
print(colors2)

print()

colors1 = ['orange', 'blue', 'green', 'red', 'yellow']
for color in colors1:
    print(color)

a = ['A', 'B', 'C', 'D', 'E']
del a[0]
print(a)
del a[0:2]
print(a)
a[0:2] = []
print(a)

print()

candies = ['딸기맛', '레몬맛', '수박맛', '우유맛', '콜라맛', '포도맛']
print("체셔고양이에게는 " + candies[0] + " 사탕을 줘요.")
print("오리에게는 " + candies[1] + " 사탕을 줘요.")
print("도도새에게는", candies[3:6], " 사탕을줘요.")

colors = ['red', 'blue', 'green']
print(colors)
colors.extend(['black', 'purple'])
print(colors)

colors = ['red', 'blue', 'green']
print(colors)
colors.insert(0, 'orange')
print(colors)

a = ['A', 'B', 'C', 'C', 'D', 'E']
print(a)
print(a.count('C'))
print(a.index('D'))
print(a)
a.remove('E')
print(a)

print()

a = [3, 1, 4, 5, 2]
print(a)
a.sort()
print(a)
a.reverse()
print(a)
print(len(a))

print()

t = [1,2,3]
print(t)

t= [1,2,3]
a,b,c = t
print(t,a,b,c)

print()

kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score,math_score,eng_score]

print(midterm_score)
print(midterm_score[0][3])

print()

color1 = ['red', 'blue', 'green']
color2 = ['orange', 'black', 'white']
print(color1 + color2)
print(len(color1))
total_color = color1 + color2
print(total_color)
print(len(total_color))

print()

colors1 = ['red', 'blue', 'green']
print(colors1 * 2)

colors1 = ['red', 'blue', 'green']
check = 'blue' in color1
check1 = 'apple' in color1
print(check)
print(check1)

color = ['orange', 'red', 'blue', 'green']
color.remove('red')
print(color)

print()

student = ['홍길동', '허난설헌', '허균']

student.append('이황')
print(student)
student.insert(3, '허균')
print(student)
print(student.count('허균'))
student.remove('홍길동')
print(student)
del student[1]
print(student)
student.reverse()
print(student)

print()

student = ['이황', '이이', '원효']
print("현재학생은 %s" %student)
a = input("전학 온 학생은 누구입니까? ")
student.append(a)
print(student)
print("번호 재정렬...")
student.sort()

b = 0
for i in student:
    b += 1
    print(b, i)

print()


a = (1,2,3,4,5)
print(a[2])
print(a[1:3])
b = list(a)
print(b)

print()

a =(1,2,3,4,5)
check_1 = 3 in a
print(check_1)
check_2 = 3 not in a
print(check_2)

print()

s = set([1,2,3,1,2,3])
print(s)


t = (1,2,3)
print(t+t, t*2)
print(len(t))

a = (1,2,3)
print(type(a))
b = 1, 2, 3
print(type(b))

print()

a = [1, '가', 2, '나']
b = tuple(a)
print(b)
c = tuple(range(1, 15, 2))
print(c)

print()

my_int = (1)
print(type(my_int))
my_tuple = (1,)
print(type(my_tuple))

print()

clovers = ('클로버1', '하트2', '클로버3')
print(clovers[1])

print()

clovers = '클로버1', '클로버2', '클로버3'
print(type(clovers))
print(clovers)

alice_blue = (240, 248, 255)
r, g, b = alice_blue
print('R:', r, 'G:', g, 'B:', b)

print()

s = {1,2,3}
print(s)
print(type(s))

s.add(5)
print(s)

s.remove(1)
print(s)

s.update([1,4,5,6,7])
s.discard(3)
print(s)

s.clear()
print(s)

print()

s1 = set([1, 2, 3, 4, 5])
s2 = set([3, 4, 5, 6, 7])

print(s1)
print(s2)

print()

print(s1.union(s2))

print(s1 | s2)

print(s1.intersection(s2))

print(s1 & s2)

print(s1.difference(s2))

print(s1 - s2)

'''

a = {1:'사과', 2:'Banana', 'three' : 3333, 'four':'4444'}
print(a)

print()

a = {(1, '가'): ['리','스','트'], (2,'나'):(2,'나'),(3, '다'):{'가','나','다','라'}}
print(a)
print(a[(1, '가')])
print(a[(3, '다')])

print()

a = {1:'사과', 2:'Banana', 'three': 3333, 'four':'4444'}
print(a[2])
print(a['three'])

print()

a = {1:'A'}
print(a)
a['Second'] = 2
print(a)
del a['Second']
print(a)

print()

clover = {'나이': 27, '직업': '병사'}
print(clover)
clover['번호'] = 9
print(clover)

print()

a = {1:'사과', 2:'Banana', 'three':3333, 'four':'4444'}
print(2 in a)
print(3333 in a)

print()

a = {1:'사과', 2:'Banana', 'three':3333, 'four':'4444'}
print(a.pop('three'))
print(a)

print()

a = {1:'사과', 2:'Banana', 'three':3333, 'four':'4444'}
print(a.pop('three'))
print(a)
a.clear()
print(a)

print()

clover = {'나이':27, '직업': '병사', '번호':9}
print(clover['번호'])
clover['번호'] = 6
print(clover['번호'])
print(clover.get('번호'))

print()

student_info = {20190012:'Tom', 20190013:'Morgan', 20190014:'Hong'}
student_info[20190012] = 'Bread'
student_info[20190015] = 'Kim'
print(student_info)

print()

country_code = {}
country_code = {"America":1, "korea":82, "china":86, "Japan":81}
print(country_code)

print()

country_code = {}
country_code = {"America":1, "korea":82, "china":86, "Japan":81}
print(country_code)
print(country_code.keys())
country_code["German"] = 49
print(country_code)
print(country_code.values())

print()

country_code = {"America":1, "korea":82, "china":86, "Japan":81}
country_code["German"] = 49
print(country_code.items())

print()

for k, v in country_code.items():
    print("Key:", k)
    print("Value", v)

print()

print("use" in country_code.keys())
print(82 in country_code.values())