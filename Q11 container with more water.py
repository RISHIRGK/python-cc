import array as arr
a=arr.array("i", [1, 8, 6, 2, 5, 4, 8, 3, 7])
ans=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        k=a[i]if a[i]<=a[j] else a[j]
        l=j-i if j>i else i
        ans= k*l if k*l > ans else ans
print(ans)