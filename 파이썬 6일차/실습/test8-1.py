# 내장함수

# abs(x) : 어떤숫자를 입력 받았을때 절대값을 돌려주는 함수

print(abs(3))

print(abs(-3))

print(abs(-1.2))

# all(x) : 반복 가능한 자료형 x를 입력 인수로 받으며 이 x가 모두 참이면 True 하나라도 0이 있으면 False를 출력

mylist = [1,2,3]
print(all(mylist))

mylist = [0,1,2] # 리스트 자료형 중에서 요소 0은 거짓
print(all(mylist))

# any(x) : x중에서 하나라도 참이 있으면 True, x가 모두 거짓일때 False
# all(x)의 반대

mylist = [0, 1, 2]
print(any(mylist))

mylist = [0, ""]
print(any(mylist))

# chr(x) : chr(i)는 아스키(ASCII)코드 값을 입력받아 그 코드에 해당하는 문자출력

print(chr(65))

print(chr(0x42))

print(chr(97))

print(chr(0x62))

print(chr(0x30))

# dir : 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다.

print(dir([1, 2, 3]))

print(dir({'1':'a'}))

# divmod(a, b) : 두개의 입력받은 값 a, b로 a를 b로 나눈 몫과 나머지를 출력

a = 7 // 4 # 7을 4로 나눈 몫
b = 7 % 4 # 7을 4로 나눈 나머지

print(a, b)

divmod(7, 4) # 7을 4로 나눈 몫과 나머지 출력
print(a, b)

# enumerate : 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력받아 인덱스값을 포함하는 enumerate 객체를 돌려준다.

for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)

# eval : eval(expression)은 실행가능한 문자열 (1 + 2, 'hi' + 'a')을 입력받아 문자열을 실행한 결과값을 돌려준다

print(eval('1 + 2'))

print(eval("'hi' + 'a'"))

print(eval('divmod(4, 3)'))


print()

# filter : 무엇인가를 걸러낸다는 뜻으로 filter 함수도 동일한 의미를 가짐

# 함수를 사용하여 걸러내기
def positive(in_list):
    result = []
    for num in in_list:
        if num > 0:
            result.append(num)

    return result

print(positive([1, -3, 2, 0, -5, 6]))

# filter를 사용하여 걸러내기
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

print()

#####

print()

# hex : 정수값을 입력받아 16진수 값으로 변환하여 돌려주는 함수

print(hex(255))

print(hex(127))

print(hex(3))

print(hex(16))

print()

# id : id(object)는 객체를 입력받아 객체의 고유주소값(래퍼런스)을 돌려주는 함수

a = 3

print(id(a))

print(id(3))

b = a

print(id(b))

print()

# int : int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자를 정수형태로 돌려주는 함수
# 정수를 입력받으면 그대로 돌려줌

print(int('3'))

print(int(3.1245))

print(int(3))

print()


###

# isinstance : isinstance(object, class) : 첫번재 인수로 인스턴스, 두번째 인수로 클래스 이름을 받는다.
# 입력으로 받은 인스턴스가 그 클래스의 인스턴스 인지를 판단하여 True / False를 돌려줌

class Person:
    pass

a = Person()
print(isinstance(a, Person)) # a라고 하는 Person 클래스의 인스턴스가 Person 클래스의 인스턴스인지 판단

b = 3
print(isinstance(b, Person))
