s="PAYPALISHIRING"

ak=""
rows=int(input("enter the number of rows"))
for i in range(rows):
    j=i
    ans=ak+s[j]
    indicator = 0
    while j<len(s):

        if indicator == 0 :
           # indicator=0 if i==0 or i==rows-1 else 1
            indicator=1
            if rows*2-2-i*2!=0 :
               j+=rows*2-2-i*2
            else :
               j+=i*2


            if j <len(s):
                ans = ans + s[j]
            else:
                pass
        else:
            indicator=0
            if i*2 != 0 :
               j += i*2
            else:
               j += j
            a=j
            if j<len(s):
                ans=ans+s[j]
            else :
                pass

    ak=ans


print(ans)