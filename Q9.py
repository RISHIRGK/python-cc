s="MCMXCIV"
def string_refining(s):
    ans=0
    if "IV" in s:
        ans+=4
        s=s.replace("IV","00")

    if "IX" in s:
        ans+=9
        s=s.replace("IX","00")

    if "XL" in s:
        ans+=40
        s=s.replace("XL","00")

    if "XC" in s:
        ans+=90
        s=s.replace("XC","00")

    if "CD" in s:
        ans+=400
        s=s.replace("CD","00")

    if "CM" in s:
        ans+=900
        s=s.replace("CM","00")

    return (ans,s)





hashmap=dict({"I": 1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"0":0})

def roman_deci(s):
    ans = hashmap[s[0]]
    b=string_refining(s)
    a=b[0]
    s=b[1]
    for i in range(1,len(s)):
        if hashmap[s[i]] >ans:
            ans=hashmap[s[i]]-ans
        elif hashmap[s[i]] <=ans:
            ans+=hashmap[s[i]]
    return ans+a
print(roman_deci("MMMCMXCIX"))
