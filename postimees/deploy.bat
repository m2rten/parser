@echo off
SET production_folder=C:\Users\marten\Production\
SET results=%production_folder%results
SET application=%production_folder%pparser

IF exist %results% ( echo %results% exists ) ELSE ( mkdir %results% && echo %results% created)
IF exist %application% ( rd /Q /S %application% && echo %application% deleted ) ELSE (echo %application% does not exist)
mkdir %application%
xcopy bin %application%
