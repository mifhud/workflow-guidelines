@.github/agents/uat.chatmode.md

First read and include the logic inside any function calls and their inner code in
{CODE}

Search inside the inner code to find test data requirements that are needed.

Use **mcp db** to retrieve the real data required (**THINK CAREFULLY ABOUT THIS — you may only use SELECT queries on mcp db**).

Create a UAT that's easy for non-programmers to understand according to the template. UAT exclude edge-cases and peformance-cases.

Provide the explanation in Indonesian, but for technical terms, do not translate them.

Save in spec/debug/uat/{feature-name}

Save it under spec/debug/uat/{feature_name/issue_name}. Do not create or modify any files other than Markdown files.
If the document is 600 lines or fewer, place everything in a new single file:
spec/debug/uat/{feature_name/issue_name}.md
If it exceeds 600 lines, split it into new multiple files numbered sequentially within the folder:
spec/debug/uat/{feature_name/issue_name}/{datemonthhourminutesecond}.md, {datemonthhourminutesecond}.md, and so on.