# Filter()
colors = ["red","green","blue","red"]

def findcolor(choice):
    return choice == "red"

print(list(filter(findcolor, colors)))

print(list(filter(lambda choice: choice =="red", colors)))


print(list(filter(lambda x: x>5, range(1,11))))
print("".join(list(filter(lambda x: x not in 'aeiouAEIOU', "AMAN"))))



