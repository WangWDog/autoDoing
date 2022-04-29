echo %*
start  python C:\AutoDoing\main.py %*
echo %ERRORLEVEL%
@echo off
rem What is this command?
EJECT d:
if errorlevel 1 goto could_not_eject
  echo Success!
  goto end
:could_not_eject
  echo Unable to eject e:
  goto end
:end