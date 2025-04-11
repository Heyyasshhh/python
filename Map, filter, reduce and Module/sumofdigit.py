import functools

def sumofdigit(n):
    n = int(n)
    sum=0
    while n>0:
        rem = n%10
        n = n // 10
        sum = sum + rem
    return sum


print(sumofdigit(159))

# print(functools.reduce(sumofdigit, ["159"])) --> Not Working way
print(list(map(sumofdigit,[123,159])))

