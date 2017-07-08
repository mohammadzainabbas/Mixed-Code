def Fibonacci(n):
    a, b,c=0, 1,0
    print("Fibonacci sequence is ")
    while a<n:
        print(a, end=' ')
        a,b,c=b,a+b,c+1
    print("\nTotal " + str(c) + " fibonacci terms under " + str(n))
while 1:
    a=int(input())
    print(Fibonacci(a))