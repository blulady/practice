import os

os.environ['PYTHONBREAKPOINT'] = 'examples.breakpoint.bp_handler'


def bp_handler(message):
    """A custom handler for breakpoint()"""
    print(message)


def find_min(nums):
    smallest = 0
    for num in nums:
        breakpoint()
        if num < smallest:
            smallest = num

    return smallest


if __name__ == '__main__':
    find_min([8, 3, 2])
