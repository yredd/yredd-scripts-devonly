# Colton Aubrey Hooke (seshormerow)
# Test user documents folder

import os
try:
    user_dir = "C:" + os.getenv('HOMEPATH') + "//Documents"
except TypeError:
    user_dir = "C:" + os.getenv('HOME') + "//Documents"
print (user_dir)