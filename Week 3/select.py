import sys

def is_valid_int(value):
    try:
        int(value)
        return True
    except(ValueError,TypeError):
        return False
    
file = sys.argv[1]
try:
    f = open(file, 'r')
    names = f.readlines()
    f.close()
except (FileExistsError, FileNotFoundError) as error:
    print(error)
    

for i in range(len(names)):
    names[i] = names[i].strip()

for arguments in sys.argv[2:]:
    print(names[int(arguments) - 1])