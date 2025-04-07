students = {
    "sid":[1,2,3],
    "names":["raj","pooja","komal"],
    "grade":["A","A+","B"]
}

s=[]
for i in students.values():
    s.append(i)

print(s)

# To fetch first Student's Details
print("Sid:",s[0][0])
print("Name:",s[1][0])
print("Grade:",s[2][0])

print()
print()
