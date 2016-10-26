# Mod directory script for Skyrim
# Windows

import os

def main():
    try:
        usr_dir = "C:" + os.getenv('HOMEPATH')
    except TypeError:
        usr_dir = "C:" + os.getenv('HOME')
    
    if os.path.exists(usr_dir + "\\The Elder Scrolls V Skyrim\\Data") == True:
        # My Documents\\My Games\\Skyrim\\Skyrimprefs.ini,
        # bEnableFileSelection needs to be set to 1 not 0
        print(usr_dir + "\\The Elder Scrolls V Skyrim\\Data")
    else:
        return 0
main()