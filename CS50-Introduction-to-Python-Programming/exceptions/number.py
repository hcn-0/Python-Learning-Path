def main():
    x = get_input()
    print(f"X is {x}")


def get_input():

    while True:
        try:
            x = int(input("What's X? "))
        except ValueError:
            print("X is not integer")

        else:
            break
    return x
main()
