# SonarQube Duplicate Blocks Identification

Access the SonarQube API to identify duplicate code blocks in the project like
https://sonarqubev8.jatismobile.com/api/duplications/show?key={SONAR_PROJECT_KEY}:{relative_file_path}

The response will contain a duplications field with the following structure like:

```json
{
    "duplications": [
        {
            "blocks": [
                {
                    "from": 123,
                    "size": 18,
                    "_ref": "1"
                },
                {
                    "from": 158,
                    "size": 18,
                    "_ref": "1"
                }
            ]
        },
        {
            "blocks": [
                {
                    "from": 236,
                    "size": 19,
                    "_ref": "1"
                },
                {
                    "from": 258,
                    "size": 19,
                    "_ref": "1"
                },
                {
                    "from": 280,
                    "size": 19,
                    "_ref": "1"
                },
                {
                    "from": 331,
                    "size": 19,
                    "_ref": "1"
                },
                {
                    "from": 15,
                    "size": 20,
                    "_ref": "2"
                }
            ]
        }
    ],
    "files": {
        "1": {
            "key": "JNS-6.5-FileValidator:src/main/java/com/jatismobile/filevalidator/db/dao/allSettingsDao.java",
            "name": "src/main/java/com/jatismobile/filevalidator/db/dao/allSettingsDao.java",
            "uuid": "AZd3c-nMBWOROL39jU4-",
            "project": "JNS-6.5-FileValidator",
            "projectUuid": "AZd3c-Hy1DL4DM4ntWpM",
            "projectName": "JNS-6.5-FileValidator"
        },
        "2": {
            "key": "JNS-6.5-FileValidator:src/main/java/com/jatismobile/filevalidator/db/dao/ByPassOJKSettingDao.java",
            "name": "src/main/java/com/jatismobile/filevalidator/db/dao/ByPassOJKSettingDao.java",
            "uuid": "AZd3c-nMBWOROL39jU5D",
            "project": "JNS-6.5-FileValidator",
            "projectUuid": "AZd3c-Hy1DL4DM4ntWpM",
            "projectName": "JNS-6.5-FileValidator"
        }
    }
}
```

Criteria:
- The duplications.blocks.size field is the number of lines, and the duplications.blocks.from field is the starting line of the duplication.
- The duplications.blocks._ref field is a reference to the file in the files field.

If there are duplicate code blocks among the following files, please merge those blocks into a single reusable function. Make sure to remove the duplicates and update the files to use the new function.