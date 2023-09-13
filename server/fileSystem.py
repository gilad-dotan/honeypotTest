import copy

# in this script we will be able to navigate the fake file system

# the files / directories are as follows:
# [name, flags : dict, the rest of the content]

def loadFiles(soc, fileSystem):
    # this variable will save the current folder we are in
    curr_folder = copy.deepcopy(fileSystem)

    soc.sendall("Please enter the system command you wish: ".encode())
    command = soc.recv(1024).decode()

    if command == "tree":
        show_tree(curr_folder)

def show_tree(curr_folder):
    show_tree(curr_folder, '')
def show_tree(curr_folder, spacer):
    for i in range(len(curr_folder - 2)):
        # printing out the files / directories names
        print(spacer, curr_folder[2 + i][0])
        if curr_folder[2 + i][1]["isDirectory"]:
            show_tree(curr_folder[2 + i], spacer + " - ")