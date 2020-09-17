import mysql.connector
myDB=mysql.connector.connect(host="localhost",user="root",passwd="",database="flights")
myData=myDB.cursor()                       # cursor fetch data from databse to myData

myData.execute("select * from employee")   # write sql code inside the bracket

for i in myData:                           # print all data from database 
    print(i)
