def draw_pattern():
    size = int(input("Enter the size of the pattern: "))
    row = 0
    
    while row < size:
        for _ in range(size):
            print("*", end="")
        print()  # New line after each row
        row += 1

if __name__ == "__main__":
    draw_pattern()