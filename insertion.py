from array import *
n=int(input("enter the range of the list :"))
a=[]*n
for i in range(n):
    x=int(input("-> "))
    a.append(x)

L=len(a)
print("list before sorted :")
print(a)

for i in range(L):
    if(i<(L-1)):
        if(a[i]>a[i+1]):
            j=i
            while(j>=0):
                if(a[j]>a[j+1]):
                    a[j],a[j+1]=a[j+1],a[j]
                j=j-1


print("list after sorted :")
print(a)


