# login information
Username = "Test"
Password = "Test"
NumOfLoginTries = 5

# file system
# flags : isDirectory, isAdministorPrivilage {only for files}, isAdminRestricted
["root", {"isDirectory" : True, "isAdministorPrivilage" : False, "isAdminRestricted" : False},
    ["users", {"isDirectory" : True, "isAdministorPrivilage" : False, "isAdminRestricted" : False},
        []]]