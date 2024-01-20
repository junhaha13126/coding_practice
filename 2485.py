def gcd(a, b):
    while(b>0):
        a, b = b, a%b
    return a


N = int(input())
arr = list()

for _ in range(N):
    arr.append(int(input()))

g = arr[1] - arr[0]
for i in range(N-1):
    g = gcd(g, (arr[i+1] - arr[i]))

cnt = 0
for i in range(N-1):
    if arr[i+1] - arr[i] != g:
        cnt += (arr[i+1] - arr[i]) // g - 1
print(cnt)