#1
num = [i for i in range(1,51) if i % 3 == 0]
print(num)
print("length of list is",len(num))

#2
words = ["python","fun","java","ai","data analysis","practice","patience","go"]
x = list(filter(lambda x: len(x)>5, words))
print(x)

#3 *args()
def calculate_tax(*salaries):
    try:
        taxes = list(map(lambda x:x*0.1, salaries))
        return sum(taxes)
    except TypeError:
        print("Invalid salary type")
    except Exception as e:
        print(e)
print(calculate_tax(5000,7000,9000))

#4 celsius to fahrenheit
celsius = [10,20,30,40,50]
fahrenheit = list(map(lambda x:(x*9/5)+32, celsius))
n = list(filter(lambda f:f>100, fahrenheit))
print(fahrenheit)
print(n)