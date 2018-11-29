import os
import shutil

import icdump

## copy files from dump to repo

for root, dirs, files in os.walk(icdump.dump):
    for f in files:
        src= os.path.join(root, f)
        fr= os.path.relpath(src, icdump.dump)
        dst= os.path.join(icdump.repo,fr)
        ##shutil.copy(src, dst)
        print(src, ' -> ', dst)

