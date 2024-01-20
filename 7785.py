n = int(input())
s = set()

for _ in range(n):
    name, record = input().split()

    if record == 'enter':
        s.add(name)
    else:
        s.remove(name)

s = list(s)
s.sort(reverse=True)
for name in s:
    print(name)