@echo off

call set

rem initialize master dump 

%GEAR% %BASE_HOT% /ConfigurationRepositoryUpdateCfg -force /DumpConfigToFiles C:\dump_master



