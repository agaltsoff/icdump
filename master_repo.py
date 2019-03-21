import os
import shutil

from icdump import base_dump, is_skipped

## delete repo files that are not in developer files from repo

dev_files= [] # contains relative paths

for root, dirs, files in os.walk(base_dump.DEVELOPER):
    for dev_f in files:
        dev_fn= os.path.join(root, dev_f)
        dev_fnrp= os.path.relpath(dev_fn, base_dump.DEVELOPER)
        dev_files.append(dev_fnrp)


for root, dirs, files in os.walk(base_dump.REPO):
    for repo_f in files:
        repo_fn= os.path.join(root, repo_f)
        repo_fnrp= os.path.relpath(repo_fn, base_dump.DEVELOPER) # developer file relative path
        if not repo_fnrp in dev_files:
            repo_fn= os.path.join(base_dump.REPO, repo_fnrp)
            os.remove(repo_fn)

## copy developer files that are not in repo from master to repo

repo_files= []

for root, dirs, files in os.walk(base_dump.REPO):
    for repo_f in files:
        repo_fn= os.path.join(root, repo_f)
        repo_fnrp= os.path.relpath(repo_fn, base_dump.REPO)
        repo_files.append(repo_fnrp)

for root, dirs, files in os.walk(base_dump.DEVELOPER):
    for dev_f in files:
        if is_skipped(dev_f): 
            continue
        dev_fn= os.path.join(root, dev_f)
        dev_fnrp= os.path.relpath(dev_fn, base_dump.DEVELOPER)
        if not dev_fnrp in repo_files:
            src= os.path.join(base_dump.MASTER, dev_fnrp)
            dst= os.path.join(base_dump.REPO, dev_fnrp)
            path= os.path.dirname(dst)
            if os.path.exists(src):
                if not os.path.exists(path):
                    os.makedirs(path)
                shutil.copy(src, dst)

        
