N=int(input())
n=N
def length(N):
    count = 0
    while True:
        c = (N//10)+(N%10)
        if c >= 10:
            c = c % 10
        N = 10*(N%10)+c
        count = count + 1
        if N == n:
            break
    return count
print(length(n))