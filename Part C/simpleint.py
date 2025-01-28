#Write a program to find the simple interest. The program should take the principle amount, rate of interest, and time as input and then display the simple interest.
def simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    print("Simple Interest: ", si)

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: "))

simple_interest(principal, rate, time)                      # Function call with the principal amount, rate of interest, and time period as arguments