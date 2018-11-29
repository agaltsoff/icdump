@echo off

call set

rem precommit dump

%GEAR% %BASE_DEV% /ConfigurationRepositoryUpdateCfg -force /DumpConfigToFiles C:\dump -update -configDumpInfoForChanges C:\dump_master\ConfigDumpInfo.xml

