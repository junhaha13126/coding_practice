N = int(input())
right_x, right_y = -100000, -100000
left_x, left_y = 100000, 100000


for _ in range(N):
    x, y = map(int, input().split())
    if x > right_x:
        right_x = x
    if y > right_y:
        right_y = y
    if x < left_x:
        left_x = x
    if y < left_y:
        left_y = y

print((right_x - left_x) * (right_y - left_y))