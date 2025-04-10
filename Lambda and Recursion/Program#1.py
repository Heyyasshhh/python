str = input("Enter String: ")
str1=str[::-1]
if len(str)<3:
    print(str)
else:
    final=str1[:3]
    final=final[::-1]
    if "ing" in final:
        ans = str + "ly"
    else:
        ans = str + "ing"
    print(ans)
