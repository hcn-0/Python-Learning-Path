def main():
    x = get_int("What's X? ")
    print(f"X is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            #x = int(input("What's X? "))
          #  print(f"X is {x}")
        except ValueError:
         #print("X is not an inteer")
         pass
        else:
          #print(f"X is {x}")
          return x
main()
