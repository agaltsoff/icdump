import os
import shutil

from icdump import base_dump

## copy files from dump to repo

for root, dirs, files in os.walk(base_dump.DEVELOPER):
    for dev_f in files:
        src= os.path.join(root, dev_f)
        srcrp= os.path.relpath(src, base_dump.DEVELOPER)
        dst= os.path.join(base_dump.REPO, srcrp)
        ##shutil.copy(src, dst)
        print(src, ' -> ', dst)

