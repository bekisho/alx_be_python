# pattern_drawing.py

# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop to handle the rows
while row < size:
    # Inner for loop to print '*' in each row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
