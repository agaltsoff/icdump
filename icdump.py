import os
import shutil
import subprocess

from codecs import open

from icdumplib import args, base_dump, is_skipped, GEAR, BASE_MASTER, BASE_DEVELOP

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

    # clear develop dir first

    if os.path.exists(base_dump.DEVELOP): shutil.rmtree(base_dump.DEVELOP)

    os.mkdir(base_dump.DEVELOP)

    subprocess.call('%s %s /ConfigurationRepositoryUpdateCfg -force'%(GEAR, BASE_DEVELOP))
    subprocess.call('%s %s /DumpConfigToFiles %s -update -configDumpInfoForChanges %s\\ConfigDumpInfo.xml'%(GEAR, BASE_DEVELOP, base_dump.DEVELOP, base_dump.MASTER))

# delete repo files that are not in develop files from repo
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

    # copy develop files that are not in repo from master to repo

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

# copy develop files to repo
def develop():
    for root, dirs, files in os.walk(base_dump.DEVELOP):
        for dev_f in files:
            if is_skipped(dev_f): 
                continue
            src= os.path.join(root, dev_f)
            srcrp= os.path.relpath(src, base_dump.DEVELOP)
            dst= os.path.join(base_dump.REPO, srcrp)
            path= os.path.dirname(dst)
            if not os.path.exists(path): os.makedirs(path)
            shutil.copy(src, dst)

#upload repo files to develop configuration
def checkout():
    subprocess.call('%s %s /LoadConfigFromFiles "%s"'%(GEAR, BASE_DEVELOP, base_dump.REPO))

# create rollback directory of master files that are developed and upload them to develop configuration
def rollback():

    rollback_path= os.path.join(args.path, 'rollback')

    if os.path.exists(rollback_path): shutil.rmtree(rollback_path)

    os.mkdir(rollback_path)

    for root, dirs, files in os.walk(base_dump.DEVELOP):
        for develop_fn in files:
            develop_rp= os.path.relpath(os.path.join(root, develop_fn), base_dump.DEVELOP)
            master_fn= os.path.join(base_dump.MASTER, develop_rp)
            rollback_fn= os.path.join(rollback_path, develop_rp)
            rollback_fn_path= os.path.dirname(rollback_fn)
            if not os.path.exists(rollback_fn_path): os.makedirs(rollback_fn_path)
            shutil.copy(master_fn, rollback_fn)

    # creating rollback file list for uploading

    file_list= ''

    for root, dirs, files in os.walk(rollback_path):
        file_list+= ' ' + ' '.join('"%s"'%(os.path.join(root, file)) for file in files if root != rollback_path and file[-3:] != 'bsl')

    list_fn= os.path.join(rollback_path, 'filelist.txt');
    with open(list_fn, 'w', 'utf-8') as list_file: list_file.write(file_list)

    subprocess.call('%s %s /LoadConfigFromFiles "%s" -Files %s'%(GEAR, BASE_DEVELOP, rollback_path, file_list))
            

def commit():
    print('Not implemented')

if __name__ == '__main__':

    cwd= os.getcwd()

    os.chdir(args.path)

    for command in args.command: locals()[command]()

    os.chdir(cwd)

    
    




















