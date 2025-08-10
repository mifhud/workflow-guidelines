After creating the unit tests, make sure they run without errors using mvn clean verify sonar:sonar, and use SonarQube MCP to get the coverage results.
Check current coverage and uncoverage tests using sonarqube mcp like
```  
{
  "component": "JNS-6.5-FileValidator:src/main/java/com/jatismobile/filevalidator/db/dao/TaskStatisticDao.java",
  "metric_keys": ["coverage", "line_coverage", "branch_coverage", "lines_to_cover", "uncovered_lines", "conditions_to_cover", "uncovered_conditions"]
}
```
To find uncovered lines, first search for lines not covered in the SonarQube HTML report at `target/site/jacoco`. If the report is not available, compare the Java file with the corresponding test file to identify uncovered code.
