def plus_two(x):
    result = x + 2
    return result

x = 3
print(plus_two(x))

# (lambda 매개변수들 : 식)(인수들)
print((lambda x : x + 2)(x))

print(list(map(plus_two, [1,2,3])))

print(list(map(lambda x : x + 2, [1,2,3])))

mylist = [4,5,6]
print(list(map(plus_two, mylist)))

print(list(map(lambda x : x + 2, mylist)))

def plus_tow():
    return 2

print(plus_tow())

print((lambda : 2)())

def plus_twos():
    return x

x = 3
print(plus_twos())

x = 2
print((lambda : x)())

a = list(range(1, 11))

# 1~10 까지의 리스트를 생성하고 리스트 가운데 3 으로 나눈 나머지가 0 인 값을 문자로 만들기
# lambda 매개변수들 : 식1 if 조건식 else 식2
print(list(map(lambda x : str(x) if x % 3 == 0 else x, a)))

def f(x):
    if x % 3 == 0:
        return str(x)
    else:
        return x

a = list(range(1, 11))
print(list(map(f, a)))

a = list(range(1, 11))

print(list(map(lambda x : str(x) if x == 1 else float(x) if x == 2 else x + 1, a)))

def f(x):
    if x == 1:
        return str(x)
    elif x == 2:
        return float(x)
    else :
        return x + 1

a = list(range(1, 11))
print(list(map(f, a)))

# filter 사용하기
# filter(함수, 반복가능 객체)
# Filter는 반복 가능한 객체에서 특정 조건에 맞는 요소만 가져옴
# Filter에 지정한 함수의 반환값이 True 일때만 해당요소를 가져옴

def f(x):
    return 5 < x < 10

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]

print(list(filter(f, a)))

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
print(list(filter(lambda x : 5 < x < 10, a)))

# reduce 사용하기
# 반복가능한 객체의 각 요소를 지정된 함수로 처리한 뒤 이전결과와 누적해서 반환

def f(x, y):
    return x + y

from functools import reduce

a = list(range(1, 6))
print(reduce(f, a))

from functools import reduce

a = list(range(1, 6))
print(reduce(lambda x, y : x + y, a))

files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']
print(list(filter(lambda x : x.find('.jpg') != -1 or x.find('.png') != -1, files)))

def f(x):
    if len(x) == 5:
        return '00' + x
    elif len(x) == 6:
        return '0' + x
    else:
        return x

files = input("파일을 입력하세요 : ").split(" ")
print(list(map(f, files)))

files = input("파일을 입력하세요 : ").split(" ")
print(list(map(lambda x : '00' + x if len(x) == 5 else '0' +x if len(x) == 6 else x, files)))
