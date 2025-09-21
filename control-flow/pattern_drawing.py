size = int(input("Enter the size of the pattern:"))
column = 0
while column < size:
    for _ in range(size):
        print("*", end="")
    print("")
    column += 1