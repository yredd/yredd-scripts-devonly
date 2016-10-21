# Colton Aubery Hooke (seshormerow)
# World of Warcraft mod directory script
# Windows

import os

def main():
    try:
        user_dir = os.getenv("ProgramW6432") # Checks if x64 OS
    except TypeError:
        user_dir = os.getenv("ProgramFiles")
    
    if os.path.exists(user_dir + "\\World of Warcraft") == True:
        print (user_dir + "\\World of Warcraft\\Interface\\AddOns") 
    else:
        return 0
main()