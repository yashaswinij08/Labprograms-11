#Write a program to display the multiplication table of a given number. The program should take the number as input and then display the multiplication table of the number.
def multiplication_table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

n = int(input("Enter a number: "))
multiplication_table(n)  # Function call with the number as argument