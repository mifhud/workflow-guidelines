VERY IMPORTANT PROMPT, PLEASE THINK HARDER ON THIS PROMPT CAREFULLY:
Before processing issues, only print or log the start time (Asia/Jakarta) using MCP time in the chat. Do not write it to a file until the issue details have been retrieved, then print the end time. Execute the issues one by one, in order. 
Before process each issues, Print/log the values formatted clearly:
    - Issue Name = The name of the issue (Get from issue file with last ongoing todo list that only marked with `[]` not `[x]` or `[-]`)
    - Start Time Issue = Asia/Jakarta using mcp time in chat, don't put to file.
    - Last Duration
After process each issues, Print/log the values formatted clearly:
    - Issue Name = The name of the issue (Get from issue file with ongoing todo list that only marked with `[]` not `[x]` or `[-]`)
    - End Time Issue = Asia/Jakarta using mcp time
    - Duration = in milisecond
    - Duration Minutes = Get from duration, then convert to minutes
    -  **IMPORTANT, PLEASE THINK HARDER ON THIS** Last Duration = Use the duration if its' a new sesion chat or the previous chat doesn't have a last duration value. If the previous chat has a last duration value, add it to the current duration.
    - Last Duration Minutes = Get from last duration, then convert to minutes
    - **IMPORTANT, PLEASE THINK HARDER ON THIS** Save the value in each issue’s attached markdown file at after the end of file during prompting, only using the following format (don't add any other text):
    ```
    Issue Name: {issue_name}
    Start Time Issue: {start_time}
    End Time Issue: {end_time}
    Duration: {duration}
    Duration Minutes: {duration_minutes}
    Last Duration: {last_duration}
    Last Duration Minutes: {last_duration_minutes}
    ```