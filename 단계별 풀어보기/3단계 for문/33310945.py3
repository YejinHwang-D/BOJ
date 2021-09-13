N, X = input().split()
N = int(N)
X = int(X)
A = list(map(int, input().split()))
for i in range(0, N):
    if A[i] < X:
        print("%d " % (A[i]), end='')