#Write a program to calculate digits, alphabets, spaces, special symbols and words in a sentence.Take the sentence from the user.
def count(s):
    d = 0
    a = 0
    sp = 0
    w = 0
    for i in s:
        if i.isdigit():
            d += 1
        elif i.isalpha():
            a += 1
        elif i.isspace():
            sp += 1
        else:
            w += 1
    print("Digits:", d)
    print("Alphabets:", a)
    print("Spaces:", sp)
    print("Special symbols:", w)
    return d, a, sp, w

s = input("Enter the sentence: ")
count(s)
