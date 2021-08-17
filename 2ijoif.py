def plus(x,y):
    return x+y

def minus(x,y):
    return x-y

def final(n):
    for i in range(n):
        z = input("연산자를 입력하시오")

        if z == "+":
            print(plus(int(input(">")),int(input(">"))))

        if z == "-":
            print(minus(int(input(">")),int(input(">"))))
