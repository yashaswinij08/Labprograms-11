#Write a program to count the number of times an element occurs in a list. Take list as input from the user.

def count(l, x):
    print(l.count(x))
    return l.count(x)


l = [ ]
inp = input("Enter the number of elements in the list: ")
for i in inp:
    l.append(inp)

x = input("Enter the element to be counted: ")
count(l, x)