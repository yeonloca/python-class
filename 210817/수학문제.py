import random

ans = int(input("몇번 반복할까요?"))

i = 0
while i < ans:
    rr = random.randint(1,10)
    ee = random.randint(1,10)
    q = int(input(str(rr)+"+"+str(ee)+"="))
    if q == rr+ee:
        i+=1
        print("맞았습니다.")
    else:
        print("틀렸습니다.")
        
