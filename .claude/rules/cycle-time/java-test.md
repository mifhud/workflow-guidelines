# Java Test Cycle Time Guidelines

## Initial Setup
Before processing issues, print or log the start time (Asia/Jakarta timezone) using MCP time in the chat. Do not write it to a file until the issue details have been retrieved, then print the end time. Execute the issues one by one, in order.

## Before Processing Each Issue
Print/log the following values with clear formatting:

- **Issue Name**: The name of the issue (obtained from issue file with the last ongoing todo list item marked with `[]`, not `[x]` or `[-]`)
- **Start Time Issue**: Asia/Jakarta timezone using MCP time in chat (do not save to file)
- **Cycle**: Set to 1 if it's a new session chat or there's no previous chat with the same issue name
- **Last Duration**: Previous accumulated duration

## During Issue Processing
When processing each issue, follow these instructions:

- **Cycle Increment**: Whenever there are steps (such as follow-up, retry, edit file, or fix errors/exceptions), increment the cycle count according to the issue's name
- **Cycle Trigger**: Increment cycle when you attempt to fix a result that failed or errored after running the `mvn` command
- **Progress Logging**: Print/log the values with clear formatting:
  - **Issue Name**: The name of the issue (obtained from issue file with ongoing todo list item marked with `[]`, not `[x]` or `[-]`)
  - **Cycle**: The current cycle value for each issue

## After Processing Each Issue
Print/log the following values with clear formatting:

- **Issue Name**: The name of the issue (obtained from issue file with ongoing todo list item marked with `[]`, not `[x]` or `[-]`)
- **End Time Issue**: Asia/Jakarta timezone using MCP time
- **Duration**: Time elapsed in milliseconds
- **Duration Minutes**: Duration converted to minutes
- **Cycle**: The final cycle value for each issue
- **Last Duration**: Use the current duration if it's a new session chat or the previous chat doesn't have a last duration value. If the previous chat has a last duration value, add it to the current duration
- **Last Duration Minutes**: Last duration converted to minutes

## Data Persistence
Save the values to each issue's attached markdown file at the end of the file during prompting, using only the following format (do not add any other text):

```
Issue Name: {issue_name}
Start Time Issue: {start_time}
End Time Issue: {end_time}
Duration: {duration}
Duration Minutes: {duration_minutes}
Cycle: {cycle}
Last Duration: {last_duration}
Last Duration Minutes: {last_duration_minutes}
```
