---
applyTo: '**'
---
Important to run this command only once at the end of the chat session.
After all issues and tasks have been processed (run only once at the end of the chat session), execute the following command in PowerShell:
```powershell
(New-Object Media.SoundPlayer "D:\02 Areas\04 Coding Tools\copilot_completed.wav").PlaySync()
```