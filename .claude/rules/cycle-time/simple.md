# Simple Cycle Time Guidelines

## Initial Setup
Before processing issues, print or log the start time (Asia/Jakarta timezone) using MCP time in the chat. Do not write it to a file until the issue details have been retrieved, then print the end time. Execute the issues one by one, in order.

## Before Processing Each Issue
Print/log the following values with clear formatting:

- **Issue Name**: The name of the issue (obtained from issue file with the last ongoing todo list item marked with `[]`, not `[x]` or `[-]`)
- **Start Time Issue**: Asia/Jakarta timezone using MCP time in chat (do not save to file)
- **Last Duration**: Previous accumulated duration

## After Processing Each Issue
Print/log the following values with clear formatting:

- **Issue Name**: The name of the issue (obtained from issue file with ongoing todo list item marked with `[]`, not `[x]` or `[-]`)
- **End Time Issue**: Asia/Jakarta timezone using MCP time
- **Duration**: Time elapsed in milliseconds
- **Duration Minutes**: Duration converted to minutes
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
Last Duration: {last_duration}
Last Duration Minutes: {last_duration_minutes}
```
