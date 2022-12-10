map={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
exceptions={4:"IV",9:"IX",40:"XL",90:"XC",400:"CD",900:"CM"}
s=int(input("enter the integer"))

ans=""

while s>0:
    a,b=0,0
    c,d="",""
    for i in map:
        if map[i]<=s:
            a=map[i]
            c=i
    for i in exceptions:
        if i<=s:
            b=i
            d=exceptions[i]
    if a>b :
        ans+=c
        s-=a
    else:
        ans += d
        s -= b

print(ans)









