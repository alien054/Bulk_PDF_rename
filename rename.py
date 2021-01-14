# Import the os module, for the os.walk function
import os
import sys

arg_count = len(sys.argv)

if arg_count > 2:
    print("""
          #usage
          rename txtName]
          
          """)
    exit

# TODO: replace special char with space

with open(sys.argv[1]+".txt", "r") as File:
    names = File.read().split("\n")
print(names)

# Set the directory you want to start from
rootDir = '.'
i = 0
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        ext = fname[-3:]
        if ext == "pdf":
            print("{}".format(fname))
            os.rename(r'{}'.format(fname), r'{}.pdf'.format(names[i]))
            i = i+1
