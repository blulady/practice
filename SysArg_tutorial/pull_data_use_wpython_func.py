import sys

while True:
    #output to stdout:
    print("Yet another iteration ...")
    try:
        # reading from sys.stdin (stope with Ctrl-D):
        number = int(input("Enter a number: "))
        if number == 0:
            print("0 has no inverse", file=sys.stderr)
        else:
            print(f"inverse of {number} is {1.0/number}")

    except(ValueError, EOFError):
        # empty string or non int value stops loop
        print("\nciao")
        break

# TO CALL FROM THE CLI
#Get-Content numbers.txt | python pull_data_use_wpython_func.py
