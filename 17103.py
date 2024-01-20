pn_list = []
check_list = [0] * 1000001


def prime_number():
    for i in range(2, 1000001):
        if check_list[i] == 0:
            pn_list.append(i)
            for j in range(2*i, 1000001, i):
                check_list[j] = 1
    return pn_list
        

T = int(input())
pn_list = prime_number()


for _ in range(T):
    cnt = 0
    N = int(input())
    for p in pn_list:
        if p > N//2:
            continue
        if check_list[N-p] == 0:
            cnt += 1
    print(cnt)