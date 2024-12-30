# ++++++++++ Files Input/Output in Python ++++++++++

# File input/output (I/O) operations allow us to read from and write to files on our system.

"""
File Modes:
    'r' – Read (default mode). Opens the file for reading. The file must exist.
    'w' – Write. Opens the file for writing (creates a new file if it doesn’t exist). If the file already exists, it truncates it.
    'a' – Append. Opens the file for appending (creates a new file if it doesn’t exist).
    'b' – Binary mode. Used with other modes for binary files (e.g., 'rb', 'wb').
    'x' – Exclusive creation. Fails if the file exists.
    't' – Text mode (default). For text files.
we can also combine modes, such as 'rb' (read binary) or 'w+' (read and write).
"""

# ++++++++++ 1. Opening a File: The open() function is used to open a file. You need to specify the file path and the mode in which to open it. The basic syntax is:
f = open("07_files_io/demo.txt", "r")
f.close()  # file should colse after opened

# ++++++++++ 2. Reading Files: Once a file is opened in read mode, we can use various methods to read its contents:

# read(size) – Reads up to size bytes from the file. If no size is specified, it reads the entire file.
f = open("07_files_io/demo.txt", "r")

content = (
    f.read()
)  # Read the entire content of the file and store it in the variable 'content'

print(content)

f.close()

# readline() – Reads a single line from the file.
f = open("07_files_io/demo.txt", "r")

line = f.readline()

print(line)

f.close()

# readlines() – Reads all lines into a list, where each element is a line.
f = open("07_files_io/demo.txt", "r")

lines = f.readlines()

for line in lines:
    print(line, end="")

f.close()

# ++++++++++ 3. Writing Files: To write data to a file, we can use the write() or writelines() method.

# write() – Writes a string to the file. Does not add a newline unless explicitly included.
f = open("07_files_io/demo.txt", "w+")

f.write("Hello World!\n")
f.write("This text is written using python's write() method.")

f.close()

# writelines() – Writes a list of strings to the file.
f = open("07_files_io/demo.txt", "w+")

lines = [
    "This is a first group of texts\n",
    "This is a second group of texts\n",
    "This is an another group of texts",
]

f.writelines(lines)

f.close()

# appending inside a file: The append() functionality is achieved by opening the file in append mode ('a'). This mode allows us to add content to the end of an existing file without overwriting its current contents.
f = open("07_files_io/demo.txt", "a")

f.write("Insert this text at the end \n")

f.close()

# ++++++++++ 4. File Context Management (Using with statement): Instead of manually closing files, Python provides a more efficient way to handle file opening and closing using the with statement. This ensures the file is automatically closed after the block is executed, even if an error occurs.
with open("07_files_io/demo.txt", "r") as files:
    content = files.read()
    print(content)

# ++++++++++ 5. File Handling for Binary Files: When working with binary files, we can open them in binary mode using the b flag.

# Reading a binary file:
with open("07_files_io/example.bin", "rb") as files:
    content = files.read()
    print(content)

# Writing to a binary file:
with open("07_files_io/example.bin", "wb") as files:
    content = bytes([41, 78, 96])
    files.write(content)

# ++++++++++ 6. Checking If a File Exists: We can check if a file exists using the os module:
import os

if os.path.exists("07_files_io/demo.txt"):
    print("File exists")
else:
    print("File does not exist")

# ++++++++++ 7. File Permissions: We can check and modify file permissions using the os module:
print(os.access("07_files_io/demo.txt", os.R_OK))  # Check read permission
print(os.access("07_files_io/demo.txt", os.W_OK))  # Check write permission

os.chmod("07_files_io/demo.txt", 0o777)  # Grant all permissions

# ++++++++++ 8. Deleting a File
os.remove("07_files_io/demo.txt")
os.remove("07_files_io/example.bin")
