students = {"sid":101, "sname":"raj", "grade":"A", "subjects":["py","js","sql"]},

'''
for i in students:
    print(i) # returns keys only 

for i in students.items():
    print(i) # returns key-value pair 

for i in students.keys():
    print(i) # returns keys only 

for i in students.values():
    print(i) # returns values only 
'''
'''
for k,v in students.items():
    print(k,":",v) # Returns key-value pair in a formatted way
'''

# Incorrect way for nesting a dictionary 
'''
students = {
    {"sid":101, "sname":"raj", "grade":"A", "subjects":["py","js","sql"]},
    {"sid":102, "sname":"komal", "grade":"A+", "subjects":["py","js","sql"]},
    {"sid":103, "sname":"pooja", "grade":"", "subjects":["py","js","sql"]}
    }
'''

'''
students = {
    101:{"sname":"raj", "grade":"A", "subjects":["py","js","sql"]},
    102:{"sname":"komal", "grade":"A+", "subjects":["py","js","sql"]},
    103:{"sname":"pooja", "grade":"B", "subjects":["py","js","sql"]}
    }
'''

'''
for i in students:
    print(i)

for i, j in students.items():
    print(i,j)
'''

'''
for i, j in students.items():
    print(i,end=" ")
    for v in j.values():
        print(v, end=" ")
    print()
'''


students = {
    101:{"sname":"raj", "subjects":{"py":90,"js":80,"sql":67}},
    102:{"sname":"komal", "subjects":{"py":90,"js":80,"sql":67}},
    103:{"sname":"pooja", "subjects":{"py":90,"js":80,"sql":67}}
    }

#WAP to find out percentage and Total marks for above students data

marks=[]
for i, j in students.items():
    print(i,end=" ")
    for k,v in j.items():
        print(v, end=" ")
        if k=="subjects":
            for m in j[k].values():
                marks.append(m)
    totalmarks=sum(marks)
    print(f"\nTotal Marks: {totalmarks}")
    per = totalmarks / len(j[k])
    print(f"Percentage: {per:0.2f}")
    marks.clear()
    print()

#OUTPUT:
'''
101 raj {'py': 90, 'js': 80, 'sql': 67} 
Total Marks: 237
Percentage: 79.00

102 komal {'py': 90, 'js': 80, 'sql': 67}  
Total Marks: 237
Percentage: 79.00

103 pooja {'py': 90, 'js': 80, 'sql': 67}  
Total Marks: 237
Percentage: 79.00
'''

