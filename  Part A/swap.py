#Write a program to swap the values of 2 variables if the second variable is greater than the first. Take the variables as input from the user.
def swap(a, b):
    if b > a:
        a, b = b, a
        print("a =", a)
        print("b =", b)
        return a, b
    else:
        print("a =", a)
        print("b =", b)
        return a, b

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
swap(a, b)