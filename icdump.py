import os
import shutil
import subprocess

from icdumplib import base_dump, is_skipped, GEAR, BASE_MASTER, BASE_DEVELOP

# initialize master dump
def setup():
    subprocess.call('%s %s /ConfigurationRepositoryUpdateCfg -force'%(GEAR, BASE_MASTER))
    subprocess.call('%s %s /DumpConfigToFiles %s'%(GEAR, BASE_MASTER, base_dump.MASTER))

# update master dump
def update():
    subprocess.call('%s %s /ConfigurationRepositoryUpdateCfg -force'%(GEAR, BASE_MASTER))
    subprocess.call('%s %s /DumpConfigToFiles %s -update'%(GEAR, BASE_MASTER, base_dump.MASTER))

# unload develop diffs from master
def precommit():

    # clear dev dir first

    if os.path.exists(base_dump.DEVELOP): 
        shutil.rmtree(base_dump.DEVELOP)

    os.mkdir(base_dump.DEVELOP)

    subprocess.call('%s %s /ConfigurationRepositoryUpdateCfg -force'%(GEAR, BASE_DEVELOP))
    subprocess.call('%s %s /DumpConfigToFiles %s -update -configDumpInfoForChanges %s\\ConfigDumpInfo.xml'%(GEAR, BASE_DEVELOP, base_dump.DEVELOP, base_dump.MASTER))

# delete repo files that are not in developer files from repo
def master():

    dev_files= [] # contains relative paths

    for root, dirs, files in os.walk(base_dump.DEVELOP):
        for dev_f in files:
            dev_fn= os.path.join(root, dev_f)
            dev_fnrp= os.path.relpath(dev_fn, base_dump.DEVELOP)
            dev_files.append(dev_fnrp)


    for root, dirs, files in os.walk(base_dump.REPO):
        if '.git' in root: continue # except git files
        for repo_f in files:
            repo_fn= os.path.join(root, repo_f)
            repo_fnrp= os.path.relpath(repo_fn, base_dump.DEVELOP) # developer file relative path
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

    for root, dirs, files in os.walk(base_dump.DEVELOP):
        for dev_f in files:
            if is_skipped(dev_f): 
                continue
            dev_fn= os.path.join(root, dev_f)
            dev_fnrp= os.path.relpath(dev_fn, base_dump.DEVELOP)
            if not dev_fnrp in repo_files:
                src= os.path.join(base_dump.MASTER, dev_fnrp)
                dst= os.path.join(base_dump.REPO, dev_fnrp)
                path= os.path.dirname(dst)
                if os.path.exists(src):
                    if not os.path.exists(path):
                        os.makedirs(path)
                    shutil.copy(src, dst)

# copy files from dump to repo
def develop():
    for root, dirs, files in os.walk(base_dump.DEVELOP):
        for dev_f in files:
            if is_skipped(dev_f): 
                continue
            src= os.path.join(root, dev_f)
            srcrp= os.path.relpath(src, base_dump.DEVELOP)
            dst= os.path.join(base_dump.REPO, srcrp)
            path= os.path.dirname(dst)
            if not os.path.exists(path):
                os.makedirs(path)
            shutil.copy(src, dst)

def commit():
    pass
    

commands= { 'setup' : setup, 'commit' : commit, 'update' : update, 'precommit' : precommit, 'master' : master, 'develop' : develop }

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(description='Выгрузка начального состояния изменений конфигурации 1С типовыми средствами')
    parser.add_argument('command', metavar='COMMAND', type=str, help='Команда', choices= ['setup','commit','update','precommit','master','develop'])

    args= parser.parse_args()

    commands[args.command]()

    
    




















