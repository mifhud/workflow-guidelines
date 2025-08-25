Retrieve duplicate line rules from URLs such as https://sonarqubev8.jatismobile.com/api/duplications/show?key={project-key}:{relative-path-file}, for example: https://sonarqubev8.jatismobile.com/api/duplications/show?key=JNS-6.5-TailCatcher:src/main/java/com/jatismobile/agais/tailcatcher/MyTailListener.java
Save respone in JSON format and use it to fix duplicate blocks in the project with key JNS-6.5-TailCatcher. Example:
```
# {Relative Path Duplicate File}
{ Response json after hit https://sonarqubev8.jatismobile.com/api/duplications/show?key={project-key}:{relative-path-file} }

# {Next Relative Path Duplicate File}
...

```