import sys
#try:
 #   print("Hello, I'm", sys.argv[1])
#except IndexError:
 #   print("Too few arguments")

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
#elif len(sys.argv) > 2:
#    sys.exit("Too many arguments")

#print("Hello, I'm", sys.argv[1])

for arg in sys.argv[1:]:
    print("Hello, I'm", arg)
