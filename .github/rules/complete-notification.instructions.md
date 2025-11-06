---
applyTo: '**'
---
Important to run this command
After all processes, issues and tasks have been processed (run only once at the end of the chat session), execute the following command:
```
powershell.exe -Command "(New-Object Media.SoundPlayer 'D:\02 Areas\04 Coding Tools\copilot_completed.wav').PlaySync()"
```
and
```
powershell.exe -Command "New-BurntToastNotification -Text 'Copilot', 'Completed'"
```