VERY IMPORTANT PROMPT, PLEASE THINK HARDER ON THIS PROMPT CAREFULLY:
Before processing issues, only print or log the start time (Asia/Jakarta) using MCP time in the chat. Do not write it to a file until the issue details have been retrieved, then print the end time. Execute the issues one by one, in order. If there's command `/reset-cycle`, Set cycle to 1 and last duration minutes to 0 and if it's a new session chat.
Before process each issues, Print/log the values formatted clearly:
    - Issue Name = The name of the issue (Get from issue file with last ongoing todo list that only marked with `[]` not `[x]` or `[-]`)
    - Start Time Issue = Asia/Jakarta using mcp time in chat, don't put to file.
    - Cycle
    - Last Duration
    - **IMPORTANT, PLEASE THINK HARDER ON THIS** Cycle = Set the cycle to 1 if it's a new session chat or there’s no previous chat with same issue name.
When processing each issue, follow these instructions:
    - Whenever there are steps (like follow‑up, retry, edit file, or fix errors/exceptions), increment the cycle count according to the issue’s name.
    - **IMPORTANT, PLEASE THINK HARDER ON THIS** A Cycle if you try to fix result Failed OR Error after run command `mvn`
    - Print/log the values formatted clearly:
      - Issue Name = The name of the issue (Get from issue file with ongoing todo list that only marked with `[]` not `[x]` or `[-]`)
      - Cycle = The cycle value of each issue
After process each issues, Print/log the values formatted clearly:
    - Issue Name = The name of the issue (Get from issue file with ongoing todo list that only marked with `[]` not `[x]` or `[-]`)
    - End Time Issue = Asia/Jakarta using mcp time
    - Duration = in milisecond
    - Duration Minutes = Get from duration, then convert to minutes
    - Cycle = The cycle value of each issue
    -  **IMPORTANT, PLEASE THINK HARDER ON THIS** Last Duration = Use the duration if its' a new sesion chat or the previous chat doesn't have a last duration value. If the previous chat has a last duration value, add it to the current duration.
    - Last Duration Minutes = Get from last duration, then convert to minutes
    - **IMPORTANT, PLEASE THINK HARDER ON THIS** Save the value in each issue’s attached markdown file at after the end of file during prompting, only using the following format (don't add any other text):
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