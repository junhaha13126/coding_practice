def f(c):
    ans = list()
    for i in range(1, c+1):
        if c % i == 0:
            ans.append(i)
    
    if sum(ans) == 2*c:
        print('{} = '.format(c), end = '')
        for i in range(len(ans)-2):
            print(ans[i], end = ' + ')
        print(ans[-2])
    else:
        print("{} is NOT perfect.".format(c))
        
        

while(True):
    c = int(input())
    if c == -1:
        break
    f(c)



 
        