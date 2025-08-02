VERY IMPORTANT PROMPT, PLEASE THINK HARDER ON THIS PROMPT CAREFULLY:
# Map Cycle Time to Table

**Map Cycle Time to Table** is a tool that extracts and organizes cycle time information from issue `.md` files into a Markdown-formatted table. The data is grouped by filename, prompt, cycle count, and total duration in minutes.

## Usage
The /map command it is not an executable or script, it is only a prompt that is used to generate the output file.
```
/map [output_directory] [output_filename] [input_directory...]
```
or

```
/map:file [output_directory] [output_filename] [input_files...]
```

## Arguments
*   **\[input\_directory\]**: Directory containing the issue `.md` files.
*   **\[output\_directory\]**: Directory where the output file will be saved.
*   **\[output\_filename\]**: Name of the output file.
*   **\[input\_files\]**: List of specific issue `.md` files to process.

## Description
This tool generates an output file in md containing a table that summarizes the cycle time information for all issue files found in the input directory.

**IMPORTANT, PLEASE THINK HARDER ON THIS** The table includes the following details:
*   Each row corresponds to one issue file.
*   **Filename Prompt** is derived from filenames referenced within each issue file, typically used for prompting.
*   **IMPORTANT, PLEASE THINK HARDER ON THIS** **Prompt** is the sum of all recorded todo list "[x] or [-]"
*   **IMPORTANT, PLEASE THINK HARDER ON THIS** **Cycle** is the sum of all recorded "Cycle"
*   **IMPORTANT, PLEASE THINK HARDER ON THIS** **Last Duration (minutes)** is the sum of all recorded "Last Duration", converted to minutes.
*  **IMPORTANT, PLEASE THINK HARDER ON THIS** Grouped by filename prompt

## Example Output

If the output file does not exist, create it with the following content:
```
## Log Cycle Time

| Prompt Filename | Prompt | Cycle Count | Last Duration (minutes) |
| --- | --- | --- |
| prompt filename | 1 | 1 | 10 |
| prompt filename | 1 | 2 | 20 |
| prompt filename | 1 | 3 | 30 |
```

If the output file already exists, append the new data to it.
```
| prompt filename | 1 | 1 | 10 |
| prompt filename | 1 | 2 | 20 |
| prompt filename | 1 | 3 | 30 |
```
