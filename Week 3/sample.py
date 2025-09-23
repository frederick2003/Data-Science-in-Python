import sys
import random

def is_valid_int(arg):
    try:
        int(arg)
    except (TypeError,ValueError) as error:
        print(error)
        sys.exit()

def valid_size(n,file_length):
    if n <= 0:
        print("n must be greater than 0")
        sys.exit()
    elif n>file_length:
        print(f"{n} is greater than the number of lines in the file")
        sys.exit()


file = sys.argv[1]
n = sys.argv[2]

is_valid_int(n)
n = int(n)
try:
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
except (FileExistsError, FileNotFoundError) as error:
    print(f"Unable to read from file: {error}")
    sys.exit()
valid_size(n,len(lines))

for i in range(len(lines)):
    lines[i] = lines[i].strip()

for i in range(n):
    rand_index = random.randint(0,len(lines)-1)
    print(lines[rand_index])
