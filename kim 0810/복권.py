import random
x = random.randint(1,100)

qhrrnjs = int(input("복권번호를 입력하시요 (0에서 99사이):"))


if qhrrnjs == x:
    print("복권번호는",x,"입니다.")
    print("상금은 100만원입니다.")
    
elif qhrrnjs % 10 == x % 10 or qhrrnjs // 10 == x // 10:
    print("복권번호는",x,"입니다.")
    print("상금은 50만원입니다.")
    
else:
    print("복권번호는",x,"입니다.")
    print("상금은 0원입니다.")
