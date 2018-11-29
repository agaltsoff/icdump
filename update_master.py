import subprocess

from icdump import base_dump, GEAR, BASE_MASTER

# initialize master dump

subprocess.call('%s %s /ConfigurationRepositoryUpdateCfg -force /DumpConfigToFiles %s -update'%(GEAR, BASE_MASTER, base_dump.MASTER))





