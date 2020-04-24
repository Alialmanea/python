#check the number you have entered is Perfect_Number or not 

def IsPerfect_Number(num):
    sum=0
    for i in  range(1,num):
        if num%i==0 :
            sum+=i
    if sum==num :
        return True
    return  False


sayi=int(input("Sayi Giriniz :"))
print(Perfect_Numbers(sayi))
