T = int(input())
for i in range(T):
    A, B = list(map(int, input().split()))
    print("Case #" + str(i + 1) + ": " + str(A + B))