def main():
    print_column(3)
    print_row(4)
    print_square(3)

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end = " ")
        print()

def print_row(weight):
    print("?" * weight)

def print_column(height):
    for _ in range(height):
        print("#")

main()
