def Palindrome(n):
    for i in range(int(len(n)/2)):
        if n[i]!=n[-i-1]:
            print(str(n) + ' is not a Palindrome')
            return
    print(str(n) + ' is a Palindrome')
    return

while 1:
    a = input()
    Palindrome(a)