size = int(input("Enter the size of the pattern: "))

while size < 1:
    size = int(input("Size must be a positive integer. Please try again: "))

row = 0
while row < size:
    col = 0
    while col < size:
        print("*", end="")
        col += 1
    print()
    row += 1
