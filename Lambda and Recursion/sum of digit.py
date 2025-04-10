#Sum of digits
n = int(input("Enter Number: "))
def sumofdigit(n):
    if n > 0:
        return n % 10 + sumofdigit(n//10)
    else:
        return 0
print(sumofdigit(n))