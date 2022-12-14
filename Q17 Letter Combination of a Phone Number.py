import array as arr
dict={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
a=(input("enter the digit"))
ans=[]
if a.isnumeric():
    if len(a)==1:
        s=dict[int(a[0])]
        for i in range(len(s)):
            ans.append(s[i])
    elif len(a)==2:
        s=dict[int(a[0])]
        t=dict[int(a[1])]
        for i in range(len(s)):
            for j in range(len(t)):
                ans.append(s[i]+t[j])
    elif len(a)==3:
        s = dict[int(a[0])]
        t = dict[int(a[1])]
        u = dict[int(a[2])]
        for i in range(len(s)):
            for j in range(len(t)):
                for k in range(len(s)):
                    ans.append(s[i] + t[j] + u[k])
    elif len(a)==4:
        s = dict[int(a[0])]
        t = dict[int(a[1])]
        u = dict[int(a[2])]
        v = dict[int(a[2])]
        for i in range(len(s)):
            for j in range(len(t)):
                for k in range(len(s)):
                    for l in range(len(s)):
                        ans.append(s[i] + t[j] + u[k] + v[l])

else :
    pass
print(ans)