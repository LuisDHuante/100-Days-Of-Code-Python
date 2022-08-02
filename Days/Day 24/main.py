# One way to open a file
file = open("file.txt")
content = file.read()
print(content)
file.close()


# Another way to open a file
with open("file.txt") as file:
    content = file.read()
    print(content)


# One way to write on a file
with open("file.txt", mode="a") as file:
    file.write("\nPat Bateman, nice to meet you")


# One way to create a new file
with open("new_file.txt", mode="w") as file:
    file.write("New text")
