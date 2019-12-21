
def RecLinearSearch(arr,l,x):
    if l<0:
        return -1
    if arr[l] == x:
        return l
    return RecLinearSearch(arr,l-1,x)


def LinearSearch(arr,l,x):
    for i in range(l):
        if arr[i]==x:
            return i
    return -1

def RecBinarySearch(arr,l,r,x):
    if l<=r:
        mid=int((l+r)/2)
        if arr[mid]==x:
            return mid
        if arr[mid]<x:
            return RecBinarySearch(arr,mid+1,r,x)
        else:
            return RecBinarySearch(arr,l,mid-1,x)
    return -1

def BinarySearch(arr,x):
    left=0
    right=len(arr)-1
    isfound=False
    while not isfound:
        if left<=right:
            mid=int((left+right)/2)
            if arr[mid]==x:
                isfound=True
                return mid
            elif arr[mid]<x:
              left=mid+1
            elif arr[mid]>x:
              right=mid-1
        else:
            isfound=True
    return -1


def main():
    arr=[-1,0,2,5,15,100]
    n=len(arr)
    x=15
    index = RecBinarySearch(arr,0,n - 1, x)
    if index != -1:
        print("Element {} is present at index {}".format (x,index))
    else:
        print("Element {} is not present".format(x))

if __name__ == '__main__':
    main()