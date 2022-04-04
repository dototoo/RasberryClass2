N = int(input())

for i in range(1,N+1):
    for t in range(N-i):
        print(' ',end="")
    for t in range(i):
        print('*',end="")
    print('')
    