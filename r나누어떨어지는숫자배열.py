def s(arr,n):
    list=[]
    for i in arr:
        if i%n==0:
            list.append(i)
    if len(list) == 0:
        list.append(-1)
    return list
