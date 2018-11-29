import os
import shutil

from icdump import base_dump

## copy developer dump files that are not in repo from master dump to repo

repo_files= []

for root, dirs, files in os.walk(base_dump.REPO):
    for f in files:
        fn= os.path.join(root, f)
        repo_files.append(os.path.relpath(fn, base_dump.REPO))

for root, dirs, files in os.walk(base_dump.DEVELOPER):
    for f in files:
        fn= os.path.join(root, f)
        fr= os.path.relpath(fn, base_dump.DEVELOPER)
        if not fr in repo_files:
            src= os.path.join(base_dump.MASTER,fr)
            dst= os.path.join(base_dump.REPO,fr)
            ##shutil.copy(src, dst)
            print(src, ' -> ', dst)

        
