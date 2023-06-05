#https://www.alpharithms.com/python-breakpoint-built-in-function-410212/
#can uncomment the bad variable name in smallestofall & run pdb to get info about error or just uncomment the breakpoint()
def find_min(nums):
    """find the smallest integer value in a list (use debugger to fix function"""
    smallest = 0
    for num in nums:
        if num < smallest:
            smallest = num
    return smallest


#find_min([9,4,2])


def find_min1(nums):
    """find the smallest integer value in a list (use debugger to fix function"""
    smallest = 0
    for num in nums:
        print('num: ', num, 'smallest:', smallest)
        if num < smallest:
            smallest = num
    return smallest


#find_min1([9,4,2])


def find_min2(nums):
    smallest = float('inf')
    for num in nums:
        print('num: ', num, 'smallest:', smallest)
        if num < smallest:
            smallest = num
            print('num smaller: reassigning value:', num)
    return smallest


find_min2([9,4,2])


def find_min3(nums):
    smallest = float('inf')
    for num in nums:

        #breakpoint()
        if num < smallest#ofall:
            smallest = num

    return smallest

find_min3([9,4,2])