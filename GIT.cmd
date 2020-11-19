@echo off
cd C:\Users\Granpepinillo\Documents\Toni\DAW_DUAL\Proyecto\proyecto_dual
git config --global user.email "apizarro@cifpfbmoll.eu"
git config --global user.name "AntoniPizarro"

:inicio
cls
set /a accion=nada
echo.
echo Usuario: %usuario%       Correo: %correo%
echo.
echo [1] Hacer push de tus archivos (actualizas tus cambios a la nube)
echo.
echo [2] Hacer pull a tus archivos (actualizas tus archivos para que coincidan con la nube)
echo.
set /p accion=...
if %accion% == 1 goto push
if %accion% == 2 goto pull
goto inicio

:push
cls
set /p msg= Mensage del commit: 
git add .
git commit -m "%msg%"
git pull
echo Actualizando local...
git push
echo Actualizando nube...
echo.
pause
goto inicio

:pull
cls
echo Actualizando local...
git pull
echo.
pause
goto inicio