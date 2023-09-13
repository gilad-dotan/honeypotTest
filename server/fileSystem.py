import json
import copy

# in this script we will be able to navigate the fake file system

# the files / directories are as follows:
# [name, flags : dict, the rest of the content]

attempts = {"exit" : 0,
            "help" : 0,
            "tree" : 0,
            "cd" : 0,
            "start" : 0,
            "rootRtrn" : 0}

def add_admin_restricted_attempt():
    with open('restrictedEntranceAttempts.txt', 'w') as convert_file:
        convert_file.write(json.dumps(attempts))

def loadFiles(soc, fileSystem, blockAdministorPermissions):
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
            soc.sendall(show_tree(soc, curr_folder, blockAdministorPermissions).encode())
        elif command.split()[0] == "cd":
            if doesFileExists(curr_folder, command.split()[1], blockAdministorPermissions) != 0 and doesFileExists(curr_folder, command.split()[1], blockAdministorPermissions) != -1 and doesFileExists(curr_folder, command.split()[1], blockAdministorPermissions)[1]["isDirectory"]:
                curr_folder = doesFileExists(curr_folder, command.split()[1], blockAdministorPermissions)
                soc.sendall("move successful".encode())
            elif doesFileExists(curr_folder, command.split()[1], blockAdministorPermissions) == -1:
                attempts["cd"] += 1
                add_admin_restricted_attempt()
                soc.sendall("ADMIN RESTRICTED FOLDER".encode())
            else:
                soc.sendall("directory not found".encode())
        elif command.split()[0] == "start":
            if doesFileExists(curr_folder, command.split()[1], blockAdministorPermissions) != 0 and doesFileExists(curr_folder, command.split()[1], blockAdministorPermissions) != -1 and not doesFileExists(curr_folder, command.split()[1], blockAdministorPermissions)[1]["isDirectory"]:
                soc.sendall(doesFileExists(curr_folder, command.split()[1], blockAdministorPermissions)[2].encode())
            if doesFileExists(curr_folder, command.split()[1], blockAdministorPermissions) == -1:
                attempts["start"] += 1
                add_admin_restricted_attempt()
                soc.sendall("ADMIN RESTRICTED FILE".encode())
            else:
                soc.sendall("file not found".encode())
        elif command == "rootRtrn":
            curr_folder = copy.deepcopy(fileSystem)
            soc.sendall("moved back to root".encode())
        else:
            soc.sendall("command not found, type 'help' for help".encode())

# returns the file / folder if found, 0 if not
def doesFileExists(curr_folder, filename, blockAdministorPermissions):
    for i in range(len(curr_folder) - 2):
        print(curr_folder[2 + i][0], filename, curr_folder[2 + i][0] == filename)
        if curr_folder[2 + i][0] == filename:
            if curr_folder[2 + i][1]["isAdminRestricted"] and blockAdministorPermissions:
                return -1
            return curr_folder[2 + i]

    return 0;

def show_tree(soc, curr_folder, blockAdministorPermissions):
    return curr_folder[0] + "\n" + show_treeSPCR(soc, curr_folder, ' - ', blockAdministorPermissions)
def show_treeSPCR(soc, curr_folder, spacer, blockAdministorPermissions):
    final_str = ""
    for i in range(len(curr_folder) - 2):
        # printing out the files / directories names
        final_str += spacer + " " + curr_folder[2 + i][0] + "\n"
        if curr_folder[2 + i][1]["isDirectory"] and not (blockAdministorPermissions and curr_folder[2 + i][1]["isAdminRestricted"]):
            final_str += show_treeSPCR(soc, curr_folder[2 + i], spacer + " - ", blockAdministorPermissions)
        elif curr_folder[2 + i][1]["isDirectory"] and blockAdministorPermissions and curr_folder[2 + i][1]["isAdminRestricted"]:
            attempts["tree"] += 1
            add_admin_restricted_attempt()
            final_str += spacer + " -  ADMIN RESTRICTED\n"

    return final_str