#Write a program to convert the first letter of a string to uppercase. Take the string as input from the user.
def convert(s):
    print(s.title())
    return s.title()

s = input("Enter the string: ")
convert(s)