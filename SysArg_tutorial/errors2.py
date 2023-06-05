import sys

save_stderr = sys.stderr
fh = open("errors2.txt", "w")
sys.stderr = fh

print >> sys.stderr, "printing to error.txt"

# return to normal:
sys.stderr = save_stderr

fh.close()