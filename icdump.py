import os
import shutil
import subprocess

from init import base_dump, GEAR, BASE_MASTER, BASE_DEVELOP

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

