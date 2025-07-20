size = input("Enter the size of the pattern: ")
size = int(size)

while size < 1:
    print("Size must be a positive integer. Please try again.")
    size = input("Enter the size of the pattern: ")
    size = int(size)
for i in range(size):
    for j in range(size):
        print("*", end="")
    print()
      
