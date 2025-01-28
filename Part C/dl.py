#Write a program to find eligibility of user to apply for a DL. The program should take the age of the user as input and then display whether the user is eligible to apply for a DL or not. A user is eligible to apply for a DL if the age is greater than or equal to 18.
def dl(age):
    if age >= 18:
        print("Eligible to apply for a DL.")
    else:
        print("Not eligible to apply for a DL.")

age = int(input("Enter your age: "))
dl(age)                     