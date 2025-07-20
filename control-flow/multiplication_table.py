def generate_table():
    number = int(input("Enter a number to see its multiplication table: "))
    
    print(f"\nMultiplication table for {number}:")
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")

if __name__ == "__main__":
    generate_table()