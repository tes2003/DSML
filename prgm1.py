n=int(input("Enter the number:"))
for i in range(2,n+1):
    flag=0
    for k in range(2,i//2+1):
        if (i%k==0):
          flag=flag+1
    if (flag>0):
        print(i)