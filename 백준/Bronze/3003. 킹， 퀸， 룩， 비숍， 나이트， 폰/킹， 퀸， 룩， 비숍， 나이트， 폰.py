chess = [1, 1, 2, 2, 2, 8]
output = ""
l = input().split()

for i in range(6):
    output += str(chess[i]-int(l[i]))+" "

print(output+'')