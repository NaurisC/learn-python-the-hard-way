from sys import argv
from os.path import exists

from_file = "test.txt" # source file
to_file = "new_test.txt" # destination file

print(f"Copying from {from_file} to {to_file}") # explain what is happening

in_file = open(from_file) # open the source file
indata = in_file.read() # read the source file and store it in a vcariable indata

print(f"The input file is {len(indata)} bytes long") # print the length of the source file

print(f"Does the outpput file exist? {exists(to_file)}") # exists() returns a boolean value if the file exists or not
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w') # open the destination file in write mode
out_file.write(indata) # write the contents of the source file that were stored in the variable indata to the destination file

print("Alright, all done.")

out_file.close() # close the destination file
in_file.close() # close the source file


