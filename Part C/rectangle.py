#Write a program to calculate dimensions of a rectangle using the formulae: perimeter = 2 * (length + breadth) and area = length * breadth. The program should take the length and breadth of the rectangle as input and then display the dimensions of the rectangle.
def rectangle(length, breadth):
    perimeter = 2 * (length + breadth)
    area = length * breadth
    print("Perimeter: ", perimeter)
    print("Area: ", area)

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
rectangle(length, breadth)                          