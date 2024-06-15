@echo off
title Kill RedstarOsu Server
:main
cls
echo ┍───────────────────────────────
echo │
echo │     Which server kill?
echo │ 
echo │   1. nginx
echo │ 
echo │   2. redis
echo │
echo │   3. all python
echo │
echo │   4. All
echo │
echo │   5. exit this program
echo │
echo ┕───────────────────────────────


set/p a=번호를 적은 후 Enter :


if %a%==1 goto nginx_kill
if %a%==2 goto redis_kill
if %a%==3 goto python_kill
if %a%==4 goto all_kill
if %a%==5 goto exit_program

:nginx_kill
cls
echo ┍───────────────────────────────
echo │
echo │     Are you sure? (nginx) (yes / no)
echo │
echo ┕───────────────────────────────
set/p confirm=yes / no   Enter :
if %confirm%==no goto main

taskkill /f /im nginx.exe
echo ┍───────────────────────────────
echo │
echo │     
echo │
echo │		Killed nginx
echo │
echo │  
echo │ 
echo ┕───────────────────────────────
pause


goto main


:redis_kill
cls
echo ┍───────────────────────────────
echo │
echo │     Are you sure? (redis) (yes / no)
echo │
echo ┕───────────────────────────────
set/p confirm=yes / no   Enter :
if %confirm%==no goto main

taskkill /f /im redis-server.exe
echo ┍───────────────────────────────
echo │
echo │     
echo │
echo │		Killed redis
echo │
echo │  
echo │ 
echo ┕───────────────────────────────
pause


goto main


:python_kill
cls
echo ┍───────────────────────────────
echo │
echo │     Are you sure? (python) (yes / no)
echo │
echo ┕───────────────────────────────
set/p confirm=yes / no   Enter :
if %confirm%==no goto main

taskkill /f /im python.exe
echo ┍───────────────────────────────
echo │
echo │     
echo │
echo │		Killed python
echo │
echo │  
echo │ 
echo ┕───────────────────────────────
pause


goto main


:all_kill
cls
echo ┍─────────────────────────────────────────────────────
echo │
echo │     Are you sure? (all with nodejs) (yes / no)     
echo │
echo ┕─────────────────────────────────────────────────────
set/p confirm=yes / no   Enter :
if %confirm%==no goto main

taskkill /f /im node.exe
taskkill /f /im nginx.exe
taskkill /f /im redis-server.exe
taskkill /f /im python.exe
::taskkill /f /im bash.exe
taskkill /f /im api
taskkill /f /im frontend
taskkill  /f /im cheesegull.exe
echo ┍──────────────────────────────────────────────────
echo │
echo │     
echo │
echo │		Killed all (kill wsl Manual)		
echo │		
echo │  
echo │ 
echo ┕──────────────────────────────────────────────────
pause


goto main


:exit_program
exit