import os
import shutil

import icdump

## copy dump files that are not in dump_repo from dump_init to dump_repo

repo_files= []

for root, dirs, files in os.walk(icdump.repo):
    for f in files:
        fn= os.path.join(root, f)
        repo_files.append(os.path.relpath(fn, icdump.repo))

for root, dirs, files in os.walk(icdump.dump):
    for f in files:
        fn= os.path.join(root, f)
        fr= os.path.relpath(fn, icdump.dump)
        if not fr in repo_files:
            src= os.path.join(icdump.master,fr)
            dst= os.path.join(icdump.repo,fr)
            ##shutil.copy(src, dst)
            print(src, ' -> ', dst)

        
