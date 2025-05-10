@echo off
REM Build and Package Fortune Teller Bot

echo Cleaning old builds...
rmdir /s /q build
rmdir /s /q dist
del /q fortune_teller.spec

echo Building executable with PyInstaller...
pyinstaller --noconsole --onefile --hidden-import=win32com.client fortune_teller.py

echo Waiting for build to finish...
timeout /t 3

echo Launching Inno Setup to compile installer...
start "" "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" "installer_script.iss"

echo Build and packaging complete!
pause
