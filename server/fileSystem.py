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
            soc.sendall(show_tree(soc, curr_folder).encode())
        elif command.split()[0] == "cd":
            if doesFileExists(curr_folder, command.split()[1]) != 0 and doesFileExists(curr_folder, command.split()[1])[1]["isDirectory"]:
                curr_folder = doesFileExists(curr_folder, command.split()[1])
                soc.sendall("move successful".encode())
            else:
                soc.sendall("directory not found".encode())
        elif command.split()[0] == "start":
            if doesFileExists(curr_folder, command.split()[1]) != 0 and not doesFileExists(curr_folder, command.split()[1])[1]["isDirectory"]:
                soc.sendall(doesFileExists(curr_folder, command.split()[1])[2].encode())
            else:
                soc.sendall("file not found".encode())
        elif command == "rootRtrn":
            curr_folder = copy.deepcopy(fileSystem)
            soc.sendall("moved back to root".encode())
        else:
            soc.sendall("command not found, type 'help' for help".encode())

# returns the file / folder if found, 0 if not
def doesFileExists(curr_folder, filename):
    for i in range(len(curr_folder) - 2):
        if curr_folder[2 + i][0] == filename:
            return curr_folder[2 + i]

    return 0;

def show_tree(soc, curr_folder):
    return curr_folder[0] + "\n" + show_treeSPCR(soc, curr_folder, ' - ')
def show_treeSPCR(soc, curr_folder, spacer):
    final_str = ""
    for i in range(len(curr_folder) - 2):
        # printing out the files / directories names
        final_str += spacer + " " + curr_folder[2 + i][0] + "\n"
        if curr_folder[2 + i][1]["isDirectory"]:
            final_str += show_treeSPCR(soc, curr_folder[2 + i], spacer + " - ")

    return final_str