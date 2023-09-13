# login information
Username = "Test"
Password = "Test"
NumOfLoginTries = 5

# file system
# flags : isDirectory, isAdministorPrivilage {only for files}, isAdminRestricted
fileSystem = ["root", {"isDirectory" : True, "isAdministorPrivilage" : False, "isAdminRestricted" : False},
                ["users", {"isDirectory" : True, "isAdministorPrivilage" : False, "isAdminRestricted" : False},
                    ["pic1", {"isDirectory" : False, "isAdministorPrivilage" : False, "isAdminRestricted" : False}, "123"],
                    ["important docs", {"isDirectory" : False, "isAdministorPrivilage" : False, "isAdminRestricted" : True}, "if the soap falls on the floor, is it dirty or clean"],
                    ["pic2", {"isDirectory" : False, "isAdministorPrivilage" : False, "isAdminRestricted" : False}, "456"]],
                ["System", {"isDirectory" : True, "isAdministorPrivilage" : False, "isAdminRestricted" : False},
                    ["Properties", {"isDirectory" : True, "isAdministorPrivilage" : False, "isAdminRestricted" : False},
                        ["hashed passowords", {"isDirectory" : True, "isAdministorPrivilage" : False, "isAdminRestricted" : True},
                            ["hashedPass1", {"isDirectory" : False, "isAdministorPrivilage" : False, "isAdminRestricted" : True}, "abc"],
                            ["hashedPass2", {"isDirectory" : False, "isAdministorPrivilage" : False, "isAdminRestricted" : True}, "def"]],
                        ["SystemPrograms", {"isDirectory" : True, "isAdministorPrivilage" : False, "isAdminRestricted" : True},
                            ["notepad", {"isDirectory" : True, "isAdministorPrivilage" : True, "isAdminRestricted" : False}]]]]]