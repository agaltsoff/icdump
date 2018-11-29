import os
import shutil

from icdump import base_dump

## copy files from dump to repo

for root, dirs, files in os.walk(base_dump.DEVELOPER):
    for f in files:
        src= os.path.join(root, f)
        fr= os.path.relpath(src, base_dump.DEVELOPER)
        dst= os.path.join(base_dump.REPO,fr)
        ##shutil.copy(src, dst)
        print(src, ' -> ', dst)

