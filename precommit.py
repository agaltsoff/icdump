import subprocess

from icdump import base_dump, GEAR, BASE_DEVELOPER

# initialize master dump

subprocess.call('%s %s /ConfigurationRepositoryUpdateCfg -force'%(GEAR, BASE_DEVELOPER))
subprocess.call('%s %s /DumpConfigToFiles %s -update -configDumpInfoForChanges %s\\ConfigDumpInfo.xml'%(GEAR, BASE_DEVELOPER, base_dump.DEVELOPER, base_dump.MASTER))





