import  random

def Swap(x,y):
    return y,x

def Shuffle_Array(arr,n):
    random.seed()
    for i in range(n-1,0,-1):
        j=random.randint(0,i+1)
        arr[i],arr[j]=Swap(arr[i],arr[j])


arr=[-1,2,5,12,45,100]
x=int(len(arr)/2)
print("====Befor Shuffle a array====")
print(arr)
Shuffle_Array(arr,x)
print("====After Shuffle array===")
print(arr)