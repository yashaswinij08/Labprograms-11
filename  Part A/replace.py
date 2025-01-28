#Write a program to convert the spaces in a string to hyphens. Take the string as input from the user.
def convert(s):
    print(s.replace(" ", "-"))
    return s.replace(" ", "-")

s = input("Enter the string: ")
convert(s)