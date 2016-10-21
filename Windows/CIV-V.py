# Civilization V mod directory finder
# Windows

import os

def main():
    try:
        user_dir = "C:" + os.getenv('HOMEPATH') + "\\Documents\\My Games\\"
    except TypeError:
        user_dir = "C:" + os.getenv('HOME') + "\\Documents\\My Games\\"
    
    if os.path.exists(user_dir + "Sid Meier's Civilization 5") == True:
        print (user_dir + "Sid Meier's Civilization 5\\MODS")
    else:
        return 0
main()