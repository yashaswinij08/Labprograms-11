#Write a program to find whether a given number is a palindrome or not. The program should take the number as input and then display whether the number is a palindrome or not.
def palindrome(n):
    og = n
    rev = 0
    while n > 0:
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    if og == rev:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")

n = int(input("Enter a number: "))
palindrome(n)                                                   