def leader(arr):
    length=len(arr)-1
    max=arr[length]
    b=[]
    b.append(arr[length])
    length-=1
    while(length>=0):
        if(arr[length]>max):
            b.append(arr[length])
            max=arr[length]
        length-=1
    left=0
    right=len(b)-1
    while(right>left):
        b[left],b[right]=b[right],b[left]
        left+=1
        right-=1
    return b
print(*leader(list(map(int,input().split()))))

 