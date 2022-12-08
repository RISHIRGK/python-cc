q="geeksforgeeks"
#input("enter the string")
# abcabcbb
# pwwkew
ans=q[0]

# for i in range(len(q)-1):
#    if q[i] != q[i+1] and q[i+1] not in ans:
#        ans=ans + q[i+1]
#    # if q[i+1] in ans :
#    #     ans=""+q[i+1]
#
# for i in range(len(q)-1):
#     for j in range(i+1,len(q)-1):
#         if q[i] != q[j] and q[i + 1] not in ans:
#             ans = q[i:j+1]
#         if q[j] in ans :
#             ans=""
#             break
i=0
for j in range(len(q)-1):
    if q[j]!=q[j+1] and q[j] not in ans:
        ans=q[i:j+1]
    elif q[j]==q[j+1]:
        i=j+1


print(ans)


