import array as arr
a=arr.array("i",[-1,2,1,-4])
target=int(input("enter the target"))
ans=100
for i in range(len(a)):
    for j in range(i+1,len(a)):
        for k in range(j+1,len(a)):
           k=a[i]+a[j]+a[k]
           e=(k-target) if k>=0 else (target-k)
           ans=k if e<ans  else ans


print(ans)

