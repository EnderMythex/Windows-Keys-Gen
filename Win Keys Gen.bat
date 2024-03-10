@echo off
cls

:Welcome
echo .......................................................................................................
echo .                                                                                                     .
echo .                            Welcome to Windows 10 / 7 / 11 Keys Generator                            .
echo .                                                - By EnderMythex                                     .
echo .                                                                                                     .
echo .                                Online : %date% %time%                  BUILD V1.0.1        .
echo .......................................................................................................
color 4

echo.
echo [!] Note: Sort valid and invalid keys as not all are valid.
echo.
pause

:Setup
cls
color a

set scriptPath=".\Win-Keys-Gen.py"

:Generate
cls
if exist %scriptPath% (
    python %scriptPath%
    echo.
    echo Operation completed successfully.
) else (
    echo Script file not found at %scriptPath%.
    echo Please check the path and try again.
    goto End
)

:Choice
echo.
set /p userChoice="Do you want to generate another key? (Y/N): "
if /I "%userChoice%" =="Y" goto Generate
if /I "%userChoice%"=="N" goto End
echo Invalid choice, please select Y (Yes) or N (No).
goto Choice

:End
echo.
echo Thank you for using Windows Keys Generator. Goodbye!
echo.
pause
