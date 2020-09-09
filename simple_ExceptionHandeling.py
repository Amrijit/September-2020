a=int(input("enter a number :"))
b=int(input("enter the divider :"))

try:                                                    
    print(a/b)

except Exception:                                       # only execute when there will be error !
    print("you can not devide by zero !")
    print("please use another value of divider :")
