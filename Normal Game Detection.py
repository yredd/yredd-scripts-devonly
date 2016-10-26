# Game detection Script
# Normal install

import os
    
def main():
    
    try:
        pro_dir = os.getenv("ProgramW6432") #Checks if x64 OS
        pro_dir = os.getenv("ProgramFiles")
    except TypeError:
        pro_dir = os.getenv("ProgramFiles")
        
    try:
        user_dir = os.getenv('HOMEPATH') + "\\AppData\\Roaming\\"
    except TypeError:
        user_dir = os.getenv('HOME') + "\\AppData\\Roaming\\"

    
    def CIV_IV(pro_dir):
        if os.path.exists(pro_dir + "\\Sid Meiers Cilization 4") == True:
            print ("CIV_IV")
    def CIV_V(pro_dir):
        if os.path.exists(pro_dir + "\\Sid Meiers Civilization 5") == True:
            print ("CIV_V")        
    def Minecraft(user_dir):
        if os.path.exists(user_dir + "\\.minecraft") == True:
            print ("Minecraft")       
    def Skyrim(pro_dir):
        if os.path.exists(pro_dir + "\\The Elder Scrolls V Skyrim") == True:
            print ("Skyrim")
    def WorldofWarcraft(pro_dir):
        if os.path.exists(pro_dir + "\\World of Warcraft") == True:
            print("WorldofWarcraft")
            
        
    CIV_IV(pro_dir)
    CIV_V(pro_dir)
    Minecraft(user_dir)
    Skyrim(pro_dir)
    WorldofWarcraft(pro_dir)
main()
    