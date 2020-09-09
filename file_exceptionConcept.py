# we know that if we open a file then we must have to close our file after we are going to close 
# our program or end our program. 


x=int(input("enter your password"))


try:
    print("{}th port is open for you !".format(100/x))

except Exception:
    print("you have entered wrong password!")

finally:                        # this block will run always no matter exception happens or not
    print("resource closed !")
