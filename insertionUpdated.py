def insertionSort(arr):
    for i  in range(1,len(arr)):
        key = arr[i]
        j=i-1
        while(j>=0 and key< arr[j]):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key


arr=[1,7,2,8,10,3]
insertionSort(arr)
print(arr)