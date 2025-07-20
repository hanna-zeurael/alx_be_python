size = input("Enter the size of the pattern: ")
size = int(size)

while size < 1:
    print("Size must be a positive integer. Please try again.")
    size = input("Enter the size of the pattern: ")
    size = int(size)

i = 0
while i < size:
    for j in range(size):
        print("*", end="")
    print()
    i += 1
