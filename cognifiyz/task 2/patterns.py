# Task 2: Generate and Print Number and Star Patterns
# Objective: Use loops to create different patterns

# --- Number Patterns ---
def pyramid(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end="")
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()

def triangle(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def inverted_triangle(rows):
    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def square(rows):
    for i in range(1, rows + 1):
        for j in range(1, rows + 1):
            print(j, end=" ")
        print()

# --- Star Patterns (Solid) ---
def star_pyramid(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

def star_inverted_pyramid(rows):
    for i in range(rows, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

def star_diamond(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

# --- Star Patterns (Hollow) ---
def hollow_pyramid(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        for j in range(1, 2 * i):
            if j == 1 or j == 2 * i - 1 or i == rows:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def hollow_diamond(rows):
    # Upper part
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        for j in range(1, 2 * i):
            if j == 1 or j == 2 * i - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    # Lower part
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i), end="")
        for j in range(1, 2 * i):
            if j == 1 or j == 2 * i - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# --- Menu for user to select pattern ---
def main():
    print("Select a Pattern Type:")
    print("1. Number Pyramid")
    print("2. Number Triangle")
    print("3. Number Inverted Triangle")
    print("4. Number Square")
    print("5. Star Pyramid")
    print("6. Star Inverted Pyramid")
    print("7. Star Diamond")
    print("8. Hollow Star Pyramid")
    print("9. Hollow Star Diamond")

    choice = int(input("Enter your choice (1-9): "))
    rows = int(input("Enter number of rows: "))

    if choice == 1:
        pyramid(rows)
    elif choice == 2:
        triangle(rows)
    elif choice == 3:
        inverted_triangle(rows)
    elif choice == 4:
        square(rows)
    elif choice == 5:
        star_pyramid(rows)
    elif choice == 6:
        star_inverted_pyramid(rows)
    elif choice == 7:
        star_diamond(rows)
    elif choice == 8:
        hollow_pyramid(rows)
    elif choice == 9:
        hollow_diamond(rows)
    else:
        print("Invalid choice!")

# Run the program
main()
