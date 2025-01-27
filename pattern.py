def ascend(inputnum):
    for i in range(1, inputnum + 1):
        for j in range(1, i+1):
             print(j , end="  ")
    print("  ")
    

def descend(inputnum):
    for i in range(1, inputnum + 1):
        for j in range(1, inputnum+2-i):
             print(j , end="  ")
    print("  ")

inputnum = int(input("Enter the number of rows: "))
pattern = input("Enter the pattern (ascend/descend): ")
if pattern == "ascend":
    ascend(inputnum)
else :
    descend(inputnum)