# SonarQube Issue Identification

Get bugs, vulnerabilities, and security hotspots from sonarqube mcp.

Develop systematic approach for fixing identified issues:

```
Issue: {Sonar Issue Name}
Error Location Code:
## {relative-file-path}:{start-line:end-line}
```
1: Code Line 1
2: Code Line 2
...
```
Fix Approach: Fix Approach
```

Save in different files based on type:
- Bug: sonar/bug-{datemonthhourminutesecond}.md
- Vulnerability: sonar/vulnerability-{datemonthhourminutesecond}.md
- Security Hotspot: sonar/security-hotspot-{datemonthhourminutesecond}.md