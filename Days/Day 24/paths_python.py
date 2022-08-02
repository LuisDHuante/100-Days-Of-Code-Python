#Paths

#Absolute Path
#Python lets you use OS-X/Linux style slashes "/" in Windows.
"""C:/Users/ldhua/Desktop/test_file.txt"""
"""/Users/ldhua/Desktop/test_file.txt"""


#Relative Path
"""../../test_file.txt"""

with open("/Users/ldhua/Desktop/test_file.txt") as f:
    content = f.read()
    print(content)