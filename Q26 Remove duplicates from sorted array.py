import array as arr
a=arr.array("i",[0,0,1,1,1,2,2,3,3,4])
def fun(a):
    i=1
    for j in range(2,len(a)):
        if a[i]!=a[j] and a[j] not in a[0:i+1]:
            a[i]=a[j]
            i+=1
    return i


print(fun(a))
print(a)