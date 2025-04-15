#WAP to generate a random password
import string
import random

allchars = (string.punctuation+string.ascii_letters+string.digits)

length = int(input("Enter length of the Password: "))
password = "".join(random.choices(allchars, k=length))
print(password)