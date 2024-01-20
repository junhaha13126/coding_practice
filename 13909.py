

N = int(input())

# 0 is close, 1 is open
window = [0] * (N+1)

for i in range(1, N+2):
    for j in range(i, N+1, i):
        window[j] = (window[j]+1) % 2
        

print(sum(window))