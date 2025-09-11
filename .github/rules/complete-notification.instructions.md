---
applyTo: '**'
---
After all issues and tasks have been processed (run only once at the end of the chat session), execute the following command in PowerShell:

```powershell
New-BurntToastNotification -Text "Copilot Completed"
```