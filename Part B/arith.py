# Write a function that takes two numbers as input and returns the sum, difference, product, quotient, remainder and exponent of the two numbers.       
def arith(a,b):
    print("Sum: ", a+b)
    print("Difference: ", a-b)
    print("Product: ", a*b)
    print("Quotient: ", a/b)
    print("Remainder: ", a%b)
    print("Exponent: ", a**b)   

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

arith(a,b)                      