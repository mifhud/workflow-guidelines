@.github/agents/uat.chatmode.md

First read and include the logic inside any function calls and their inner code in
{CODE}

Search inside the inner code to find test data requirements that are needed.

Use **mcp db** to retrieve the real data required (**THINK CAREFULLY ABOUT THIS — you may only use SELECT queries on mcp db**).

Create a UAT that's easy for non-programmers to understand according to the template. UAT exclude edge-cases and peformance-cases.

Provide the explanation in Indonesian.

Save in spec/debug/uat/{feature-name}