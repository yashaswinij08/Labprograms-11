# Write a Python program to solve a quadratic equation of the form ax^2+bx+c=0. The program should take the values of a, b, and c as input and then display the values of the roots of the equation. You may use the math module in your program.   
def check(a, b, c):
    if d == 0:
        x = -b / (2 * a)
        print("The equation has one real root: ", x)
    elif d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print("The equation has two real roots: ", x1, "and", x2)
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print("The equation has two complex roots: ", x1, "and", x2)

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
d = b ** 2 - 4 * a * c

check(a, b, c)