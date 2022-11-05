score=int(input())
if score in range(90,101):
    print('A')
if score in range(80,90):
    print('B')
if score in range(70,80):
    print('C')
if score in range(60,70):
    print('D')
if score<60:
    print('F')