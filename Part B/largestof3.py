#Write a program to find the largest of three numbers. The program should take the three numbers as input and then display the largest number.
def largest_of_three(a, b, c):
    if a >= b and a >= c:
        print("Largest number: ", a)
    elif b >= a and b >= c:
        print("Largest number: ", b)
    else:
        print("Largest number: ", c)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
largest_of_three(a, b, c)   # Function call with the three numbers as arguments