import os
import shutil

from icdump import base_dump, is_skipped

# copy files from dump to repo

for root, dirs, files in os.walk(base_dump.DEVELOPER):
    for dev_f in files:
        if is_skipped(dev_f): 
            continue
        src= os.path.join(root, dev_f)
        srcrp= os.path.relpath(src, base_dump.DEVELOPER)
        dst= os.path.join(base_dump.REPO, srcrp)
        path= os.path.dirname(dst)
        if not os.path.exists(path):
            os.makedirs(path)
        shutil.copy(src, dst)

