import subprocess

from icdump import base_dump, GEAR, BASE_DEVELOPER

# initialize master dump

# %GEAR% %BASE_DEV% /ConfigurationRepositoryUpdateCfg -force /DumpConfigToFiles C:\dump -update 

subprocess.call('%s %s /ConfigurationRepositoryUpdateCfg -force /DumpConfigToFiles %s -update -configDumpInfoForChanges %s\\ConfigDumpInfo.xml'%(GEAR, BASE_DEVELOPER, base_dump.DEVELOPER, base_dump.MASTER))





