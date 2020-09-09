n=int(input("enter a number to divide 100 :"))

try:
    print("your new value is {}".format(100/n))
    print("your access is granted to the file ")
    password=int(input("enter your login id "))
    print("no {} is online !".format(password))

except ZeroDivisionError:
    print("you cannot devide by zero !!!")

except ValueError:
    print("the type of your value is not correct !!!")

except Exception as e :
    print("there is an error ! please check this =>> ",e)

finally:
    print("your file is closed successfully ")