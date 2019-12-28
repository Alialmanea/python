
def frequencyofelement(arr,n,x):
    count=0
    for i in range(n):
        if arr[i]==x:
            count+=1

return count

def main():
    arr=[1,2,3,4,5,6,6,1,2,3,4,4,23,3,3,1,2,12,0,1]
    x=frequencyofelement(arr,len(arr),1)
    print("The frequency of element {} is : {}".format(1,x))




if __name__ == '__main__':
    main()

