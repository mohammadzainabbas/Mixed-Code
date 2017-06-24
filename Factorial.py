def Factorial(n):
    if n==1:
        return 1
    else:
        return n * Factorial(n-1)

a = int(input())

print('Factorial of ' + str(a) + ' is ' + str(Factorial(a)))