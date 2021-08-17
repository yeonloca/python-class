import random
list1=[]
list2=[]

# 복권 당첨번호 뽑기
i = 0
while i < 5:
    x = random.randint(1,10)
    if x not in list1:
        list1.append(x)
        i+=1

# 사용자의 번호 입력
i = 0
while i < 5:    
    x = int(input("숫자를 입력하세요:"))
    if x not in list2:
        list2.append(x)
        i+=1
    else:
        print("전에 입력했습니다.")
count = 0
for i in list1:
    for j in list2:
        if i == j:
            count +=1

if count == 5:
    print("1등")
elif count == 4:
    print("2등")
elif count == 3:
    print("3등")


