import sys

def overlap(file1, file2):
    intersection = set()
    f1 = open(file1, "r")
    f2 = open(file2, "r")
    f1_nums = f1.readlines()
    f2_nums = f2.readlines()
    f1.close()
    f2.close()

    for i in range(len(f1_nums)):
        f1_nums[i] = int(f1_nums[i].strip())
    f1_nums_set = set(f1_nums)

    for i in range(len(f2_nums)):
        f2_nums[i] = int(f2_nums[i].strip())
    
    for num in f2_nums:
        if num in f1_nums_set:
            intersection.add(num)
    sorted_list = sorted(intersection)
    print(sorted_list)
    
    





file1 = sys.argv[1]
file2 = sys.argv[2]
overlap(file1,file2) 