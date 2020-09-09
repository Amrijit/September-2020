n= int(input("enter a number :"))

try:
    print("your new value is :{}".format(1000/n))

except ZeroDivisionError:
    print("you cannot devide by zero !!!!")

finally:
    print("have a nice day @")
