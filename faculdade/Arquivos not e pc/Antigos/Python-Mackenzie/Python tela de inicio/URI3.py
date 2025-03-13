N = []
v = int(input())
N.append(v)
for i in range(10):
    v = v * 2
    N.append(v)
    print('N[{}] = {}'.format(i,N[i]))
    
