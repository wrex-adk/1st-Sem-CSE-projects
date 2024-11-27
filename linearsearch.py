def search(list,n,key):
    for i in range(0,n):
        if (list[i]==key):
            return i
    return -1
list=[1,2,3,4,5,6,7]
n=len(list)
key=3
result=search(list,n,key)
if result==-1:
    print("The number not found")
else:
    print("element found at position",result+1)