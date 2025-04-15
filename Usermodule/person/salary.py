import emp 
import days 

def calculatesalary():
    perday_pay = 1000
    totalsalary = perday_pay * days.totaldays()
    print(f"Name: {emp.fullname()} and Salary: {totalsalary}")