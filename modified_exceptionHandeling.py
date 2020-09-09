a=int(input("enter a number :"))
b=int(input("enter the divider value :"))

try:
    print(a/b)

except Exception as e:
    print("hey! you cannot divide by zero, look in more details :")
    print("the exception is =>> ",e)
