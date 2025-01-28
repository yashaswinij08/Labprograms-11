num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

print("The first number before swapping is :",num1)
print("The second number before swapping is :",num2)

num1 = num2 + num1
num2= num1 - num2
num1 = num1 - num2


print("The first number after swapping is :",num1)
print("The second number after swapping is :",num2)