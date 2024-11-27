def binary(arr,x):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(high+low)//2
        if arr[mid]<x:
            low=mid+1
        elif arr[mid]>x:
            high=mid-1
        else:
            return mid
        
    return -1
arr=[1,2,3,4,5]
a=int(input("enter a number: "))
res=binary(arr,a)
if res==-1:
    print("not in array")
else:
    print("found at position",res+1)
