import os
import shutil
import subprocess

from icdump import base_dump, GEAR, BASE_DEVELOP

# initialize master dump

# clear dev dir first

if os.path.exists(base_dump.DEVELOP): 
    shutil.rmtree(base_dump.DEVELOP)

os.mkdir(base_dump.DEVELOP)

subprocess.call('%s %s /ConfigurationRepositoryUpdateCfg -force'%(GEAR, BASE_DEVELOP))
subprocess.call('%s %s /DumpConfigToFiles %s -update -configDumpInfoForChanges %s\\ConfigDumpInfo.xml'%(GEAR, BASE_DEVELOP, base_dump.DEVELOP, base_dump.MASTER))





