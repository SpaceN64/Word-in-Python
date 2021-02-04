# Imports
import time

# File Types
file_docx = ["Docx", "docx", "1"]
file_txt = ["TxT", "Txt", "txt", "2"]
file_doc = ["Doc", "DOC", "doC", "doc", "3"]

# Way to exit
leave = ["exit", "exit()", "Exit", "Exit()"]

# Intro
print("""
Word for
 Python
  v2.0
""")

time.sleep(1.5)

# File type Program
print("""Please choose a file type:\n 1 docx\n 2 txt\n 3 doc\n
""")
file_type = input(">>> ")

if file_type in file_docx:
    f = open("Untitled.docx", "w")
elif file_type in file_txt:
    f = open("Untitled.txt", "w")
elif file_type in file_doc:
    f = open("Untitled.doc", "w")

print('Remember, press enter and then type "exit()" to exit.')
time.sleep(1)

enter = input("""Press enter to continue...
""")

# typing Part
print("""Start Typing: """)
while True:
    write = input(""" \n """)
    if write in leave:
        f.close()
        exit()
    else:
        f.write(write)
