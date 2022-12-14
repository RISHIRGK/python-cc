import array as arr
a=arr.array("i",[-1,0,1,2,-1,-4])
b=arr.array("i")
# print(b)
l=len(a)
n=0
for i in range(l):
    for j in range(i+1,l):
        for k in range(j+1,l):
            m=a[i]+a[j]+a[k]
            if m==0:
                print(i,j,k)
