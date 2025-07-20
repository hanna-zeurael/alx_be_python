# pattern_drawing.py

size = input("Enter the size of the pattern: ")
size = int(size)

while size < 1:
    print("Size must be a positive integer. Please try again.")
    size = input("Enter the size of the pattern: ")
    size = int(size)

i = 0
while i < size:
    j = 0
    while j < size:
        print("*", end="")
        j += 1
    print()
    i += 1
