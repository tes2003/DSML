n=int(input("Enter the order:"))
num1=0
num2=1
count=2
print(num1)
print(num2)
while count<n:
    next=num1+num2
    print(next)
    num1=num2
    num2=next
    count=count+1