aa, bb, cc = map(int, input().split())
a = min(aa, bb, cc)
c = max(aa, bb, cc)
b = aa+bb+cc - a - c

while c >= (a+b):
    c -= 1

print(a+b+c)

            
