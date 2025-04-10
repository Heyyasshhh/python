# Lambda function

show = lambda: print("lambda function")
show()


# lambda function with argument
#TYPE #1
addition = lambda a,b: print("Addition:",a+b)
addition(4,5)

#TYPE #2
(lambda a,b: print("Addition:",a+b))(45,54)


# Lambda with if else 

#WAP to check number is positive or negative by using lambda
(lambda n: print(n,"is a +ve number") if n>0 else  print(n,"is -ve number"))(-159)


# Lambda with Loop
loop = lambda : [print(i,end=" ") for i in range(1,11)]
loop()
print()

print(list(map(lambda i:i, range(1,11))))
print(list(map(lambda i:i**2, range(1,11))))