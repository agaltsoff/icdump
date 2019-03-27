import subprocess

from init import base_dump, GEAR, BASE_MASTER

# initialize master dump
def setup():
    subprocess.call('%s %s /ConfigurationRepositoryUpdateCfg -force'%(GEAR, BASE_MASTER))
    subprocess.call('%s %s /DumpConfigToFiles %s'%(GEAR, BASE_MASTER, base_dump.MASTER))



