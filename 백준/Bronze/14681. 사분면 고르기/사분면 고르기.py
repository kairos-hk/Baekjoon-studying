X = int(input())
Y = int(input())
if X >= 1 and Y >= 1:
    print("1")
elif X <= -1 and Y >= 1:
    print("2")
elif X <= -1 and Y <= -1:
    print("3")
else:
    print("4")