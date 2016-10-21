# Sid Meier's Civilivation IV mod directory finder
# Windows

import os

def main():

    try:
        user_dir = os.getenv("ProgramW6432") # Checks if x64 OS
        user_dir = os.getenv("ProgramFiles")
    except TypeError:
        user_dir = os.getenv("ProgramFiles")
        
    if os.path.exists(user_dir + "\\Sid Meiers Civilization 4") == True:
        print (user_dir + "\\Sid Meiers Civilization 4\\Mods")
    else:
        return 0
main()