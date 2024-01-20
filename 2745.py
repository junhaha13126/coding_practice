N, B = input().split()
B = int(B)

ans = 0
b = 1
n = len(N)
for c in range(n-1, -1, -1):
    if ord(N[c]) < 58:
        ans = ans + int(N[c]) * b
    else:
        ans = ans + (ord(N[c]) - 55) * b
    b = b * B
    
print(ans)
