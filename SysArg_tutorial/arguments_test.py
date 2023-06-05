import sys

#list of arguments:
print(sys.argv)

#or it can be iterated via a for loop:

for i in range(len(sys.argv)):
    if i == 0:
        print("Function name: ", sys.argv[0])
    else:
        print(f'{i:1d}. argument: {sys.argv[i]}')


# TO CALL FROM THE CLI
#python arguments_test.py  a b c d e