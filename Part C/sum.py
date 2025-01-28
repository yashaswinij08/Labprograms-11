#Write a program to calculate the sum of digits of a number. The program should take the number as input and then display the sum of the digits of the number.
input_number = int(input("Enter a number: "))
sum = 0

while input_number > 0:
    sum += input_number % 10
    input_number = input_number // 10

print("Sum of digits: ", sum)                           
