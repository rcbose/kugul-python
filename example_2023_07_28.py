
import sys
print (sys.argv[2])
file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"r")
print (file1.read())
print (file2.read())
