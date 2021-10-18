'''
file = open('hello.txt', 'w')
for i in range(5):
    file.write('Hello python\n')
file.close()

print()

file = open('hello.txt', 'a')
for i in range(5):
    file.write('====Hello python\n')
file.close()

print()

file = open('hello.txt', 'r')
s = file.read()
print(s)
file.close()

print()

# with open 사용하기
# 파일객체.close() 생략가능
# 파이썬에서 객체를 자동으로 닫아줌

with open('hello.txt', 'w') as file:
    file.write('hello Python')

# 파일 읽어오기
# 파일객체 = open(파일이름, 'r')
# 파일객체.reead()
# 파일객채.close()

with open('hello.txt', 'r') as file:
    s = file.read()
    print(s)

# 반복문을 사용하여 여러줄의 문자열을 파일에 쓰기

with open('hello.txt', 'w') as file:
    for i in range(10):
        file.write('{} : Hello Python\n'.format(i + 1))

# 지정된 파일 읽어오기

with open('hello.txt', 'r') as file:
    s = file.read()
    print(s)

# 리스트에 있는 문자열을 파일에 쓰기

lines = ['Hello\n', "I Love Fruits\n", "Python"]

with open('hello.txt', 'w') as file:
    file.writelines(lines)

with open('hello.txt', 'r') as file:
    s = file.read()
    print(s)

# 파일의 내용을 한줄식 리스트로 가져오기
# 변수 = 파일객체.readlines()

with open('hello.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

# 파일의 내용을 한줄씩 읽어오기
# 변수 = 파일객체.readlines()

with open('hello.txt', 'r') as file:
    line = None
    while line != '':
        line = file.readline()
        print(line, end="")


with open('hello.txt', 'r') as file:
    line = None
    while line != '':
        line = file.readline()
        print(line.strip('\n'))

import os
os.mkdir('test')

import os
if not os.path.isdir('test'):
    os.mkdir('test')

import pickle
a = {1:"a", 2:"b", 3:"c"}; b = [1, 2, 3, 4, 5]

with open('picklefile.bin', 'wb') as f:
    pickle.dump(a, f)
    pickle.dump(b, f)

import pickle

with open('picklefile.bin', 'rb') as f:
    data = pickle.load(f)
    print(data)

import pickle

f = open("list.pickle", 'wb')
test = [1, 2, 3, 4]
pickle.dump(test, f)
f.close()

import pickle
f = open("list.pickle", 'rb')
test_pickle = pickle.load(f)
print(test_pickle)
f.close()

hp = 300
hit = ""
print("현재 체력은 %d 입니다." % hp)

while hit != "save" and hp > 0:
    hit = input("데미지를 몇 입었습니까 : ")
    if hit == "save":
        f = open('save.txt', 'w')
        f.write(str("체력이 %d 남았습니다." % hp))
        f.close()

    else:
        hit = int(hit)
        hp = hp - hit
        print("체력이 %d 남았습니다." % hp)


hp = 300
hit = ""

try:
    f = open('save.txt', 'r')
    hp = int(f.read())
    f.close()
    print("save된 파일을 불러오는중...")

except:
    print("세이브된 파일을 찾을 수 없습니다.")


print("현재 체력은 %d 입니다." % hp)
while hit != "save" and hp > 0:
    hit = input("데미지를 몇 입었습니까 : ")
    if hit == "save":
        f = open('save.txt', 'w')
        f.write(str(hp))
        f.close()

    else:
        hit = int(hit)
        hp = hp - hit
        print("체력이 %d 남았습니다." % hp)

nation = ["한국", "미국", "일본", "중국", "러시아", "베트남"]
a = "a"

while a:
    if a == 'q':
        break

    a = input("나라 이름을 입력하세요 : ")

    try:
        print(nation.index(a))

    except ValueError as e:
        f = open("ErrorLog.txt", "a")
        f.write("%s\n" % a)
        f.close()
        print("%s 국가는 리스트에 존재하지 않습니다. 로그기록" % e)

import random

with open('score.txt', 'w', encoding='utf-8') as score:
    for n in range(6):
        score.write(str(random.randint(50, 100)) + "\n")


f = open("score.txt", 'r')
score = f.readlines()
score = list(map(int, score))

score_sum = 0
for i in score:
    score_sum = score_sum + i

score_average = score_sum / len(score)

print("전체 합은 %d 입니다." % score_sum)
print("전체의 평균은 %d 입니다." % score_average)
'''
import random

ch = ["삐", "빠"]

with open('replace.txt', 'w', encoding='utf-8') as pipa:
    for n in range(100):
        pipa.write(random.choice(ch)+ "")


f = open('replace.txt', 'r', encoding='utf-8')
letter = f.read()
f.close()

letter = letter.replace("삐", "빠")

f = open('replace.txt', 'w')
f.write(letter)
f.close()