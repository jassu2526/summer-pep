# def drop_minimum(*args):
#     n = list(args)
#     n.remove(min(n))
#     return n
# print(drop_minimum(5,-2,8,4,-5,7,10))

def employee(**salary):
    total=0
    highest_name="" 
    highest_salary=0
    for i in salary:
        total = total + salary[i]
        if salary[i]>highest_salary:
            highest_salary=salary[i]
            highest_name=i
    average = total / len(salary)
    return average,highest_name
average,name = employee(john=50000,jill=70000,mark=60000)
print("average salary is",average)
print(name,"gets highest salary")