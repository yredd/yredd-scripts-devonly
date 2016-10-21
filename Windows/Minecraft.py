# Colton Aubrey Hooke (seshormerow)
# Minecraft mod directory finder
# Windows

import os

def main():
    try:
        user_dir = "C:" + os.getenv('HOMEPATH') + "\\AppData\\Roaming\\"
    except TypeError:
        user_dir = "C:" + os.getenv('HOME') + "\\AppData\\Roaming\\"
    
    if os.path.exists(user_dir + "Minecraft") == True:
        print (user_dir + "Minecraft\\mods")
    else:
        return 0
main()