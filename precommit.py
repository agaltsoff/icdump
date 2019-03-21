import os
import shutil
import subprocess

from icdump import base_dump, GEAR, BASE_DEVELOPER

# initialize master dump

# clear dev dir first

if os.path.exists(base_dump.DEVELOPER): 
    shutil.rmtree(base_dump.DEVELOPER)

os.mkdir(base_dump.DEVELOPER)

subprocess.call('%s %s /ConfigurationRepositoryUpdateCfg -force'%(GEAR, BASE_DEVELOPER))
subprocess.call('%s %s /DumpConfigToFiles %s -update -configDumpInfoForChanges %s\\ConfigDumpInfo.xml'%(GEAR, BASE_DEVELOPER, base_dump.DEVELOPER, base_dump.MASTER))





