# Game detection Script
# Steam install

import os

def main():
    
    try:
        pro_dir = "C:" + os.getenv("ProgramW6432")
        pro_dir = "C:" + os.getenv("ProgramFiles") + "\\Steam\\steamapps\\common\\"
        pro_dir_gm = "C:" + os.getenv("ProgramFiles") + "\\Steam\\steamapps\\"
    except TypeError:
        pro_dir = "C:" + os.getenv("ProgramFiles") + "\\Steam\\steamapps\\common\\"
        pro_dir_gm = "C:" + os.getenv("ProgramFiles") + "\\Steam\\steamapps\\"
        
    
    def CIV_IV(pro_dir):
        if os.path.exists(pro_dir + "Sid Meier's Civilization IV") == True:
            print("CIV_IV")
    def CIV_V(pro_dir):
        if os.path.exists(pro_dir + "Sid Meier's Civilization V") == True:
            print("CIV_V")
    def garrysmod(pro_dir):
        if os.path.exists(pro_dir_gm + "garrysmod\\garrysmod") == True:
            print("garrysmod")
    def Skyrim(pro_dir):
        if os.path.exists(pro_dir + "skyrim") == True:
            print("Skyrim")
    def TF2(pro_dir):
        if os.path.exists(pro_dir + "Team Fortress 2\\tf") == True:
            print("TF2")
    
    
    CIV_IV(pro_dir)
    CIV_V(pro_dir)
    garrysmod(pro_dir_gm)
    Skyrim(pro_dir)
    TF2(pro_dir)
main()