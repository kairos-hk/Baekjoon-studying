a, b= map(int, input().split())

if a>=0 and b>=45 :
    a = int(a)    
    b = int(b-45)
    print(a, b)
elif a>=1 and b <45 :
    a = int(a-1)
    b = int(b+15)
    print(a,b)
else :
    a = int(a+23)
    b = int(b+15)
    print(a,b)