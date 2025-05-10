; Inno Setup script for Fortune Teller Bot

[Setup]
AppName=Fortune Teller Bot
AppVersion=1.0
DefaultDirName={autopf}\FortuneTeller
DefaultGroupName=Fortune Teller
UninstallDisplayIcon={app}\fortune_teller.exe
OutputDir=dist
OutputBaseFilename=FortuneTellerInstaller
Compression=lzma
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64compatible

[Files]
Source: "dist\fortune_teller.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Fortune Teller"; Filename: "{app}\fortune_teller.exe"; WorkingDir: "{app}"
Name: "{userstartup}\Fortune Teller"; Filename: "{app}\fortune_teller.exe"; WorkingDir: "{app}"

[Run]
Filename: "{app}\fortune_teller.exe"; Description: "Run Fortune Teller"; Flags: nowait postinstall skipifsilent
