name=input().lower()
a={}
a[' ']=0
for i in range(1,27):
    a[chr(i+96)]=i
n=0
for i in name:
    n=n+a[i]
while n>10:
    ns=str(n)
    sum=0
    for i in ns:
        t=int(i)
        sum=sum+t
    n=sum
print(n)
