@echo off

call set

rem update master dump 

%GEAR% %BASE_HOT% /ConfigurationRepositoryUpdateCfg -force /DumpConfigToFiles C:\dump_master -update 



