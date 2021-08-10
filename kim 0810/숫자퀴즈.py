import random as r
x = r.randint(1,100)
c = 0
while True:
    answer = int(input("숫자입력:"))
    if x == answer:
        break
    if x > answer:
        print("up")
    if x < answer:
        print("down")
    c+=1
print("맞았습니다. 시도횟수:",c)


