After process each issues, Print/log the values formatted clearly:
    - Issue Name = The name of the task
    - End Time Issue = Asia/Jakarta using mcp time
    - Duration in milisecond
    - Cycle = The cycle value of each task
    - Last Duration = Use the duration if the previous chat doesn't have a last duration value. If the previous chat has a last duration value, add it to the current duration.
    - Last Duration Minutes = Get from last duration, then convert to minutes
    - **IMPORTANT, PLEASE THINK HARDER ON THIS** Only print or log (don't save to file) the value in each issue’s attached markdown file at after the end of file during prompting, only using the following format (don't add any other text):
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