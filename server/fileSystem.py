import copy

# in this script we will be able to navigate the fake file system

# the files / directories are as follows:
# [name, flags : dict, the rest of the content]

def loadFiles(soc, fileSystem):
    commands_list = ["exit", "help", "tree", "cd", "start", "rootRtrn"]

    # this variable will save the current folder we are in
    curr_folder = copy.deepcopy(fileSystem)

    while True:
        soc.sendall("-> ".encode())
        command = (str)(soc.recv(1024).decode())

        if command == "exit":
            return 1
        elif command == "help":
            soc.sendall(", ".join(commands_list).encode())
        elif command == "tree":
            show_tree(curr_folder)
        elif command.split()[0] == "cd":
            if doesFileExists(curr_folder, command.split()[1]) != 0 and doesFileExists(curr_folder, command.split()[1])[1]["isDirectory"]:
                curr_folder = doesFileExists(curr_folder, command.split()[1])
            else:
                soc.sendall("directory not found".encode())
        elif command.split()[0] == "start":
            if doesFileExists(curr_folder, command.split()[1]) != 0 and not doesFileExists(curr_folder, command.split()[1])[1]["isDirectory"]:
                soc.sendall(doesFileExists(curr_folder, command.split()[1])[2].encode())
            else:
                soc.sendall("file not found".encode())
        elif command == "rootRtrn":
            curr_folder = copy.deepcopy(fileSystem)

# returns the file / folder if found, 0 if not
def doesFileExists(curr_folder, filename):
    for i in range(len(curr_folder) - 2):
        if curr_folder[2 + i][0] == filename:
            return curr_folder[2 + i]

    return 0;

def show_tree(curr_folder):
    print(curr_folder[0])
    show_treeSPCR(curr_folder, ' - ')
def show_treeSPCR(curr_folder, spacer):
    for i in range(len(curr_folder) - 2):
        # printing out the files / directories names
        print(spacer, curr_folder[2 + i][0])
        if curr_folder[2 + i][1]["isDirectory"]:
            show_treeSPCR(curr_folder[2 + i], spacer + " - ")