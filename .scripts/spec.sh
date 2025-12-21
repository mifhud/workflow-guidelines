#!/bin/bash

# 1. Create directory structure
# -p ensures parent folders are created if they don't exist
mkdir -p "spec/debug"
mkdir -p "spec/issue"
mkdir -p "spec/plan"
mkdir -p "spec/design"
mkdir -p "spec/archive/debug"
mkdir -p "spec/archive/issue"
mkdir -p "spec/archive/plan"
mkdir -p "spec/archive/design"

echo "✅ Directories created successfully."

# 2. Update or create .gitignore
GITIGNORE=".gitignore"
ENTRY="spec/archive"
SETTINGS_ENTRY=".settings"
MCP_CLAUDE_ENTRY=".mcp.json"
OPENCODE_ENTRY="opencode.json"

if [ -f "$GITIGNORE" ]; then
    # If the file exists, add a newline and the entries to ensure they don't merge with existing text
    echo "" >> "$GITIGNORE"
    echo "$ENTRY" >> "$GITIGNORE"
    echo "$SETTINGS_ENTRY" >> "$GITIGNORE"
    echo "$MCP_CLAUDE_ENTRY" >> "$GITIGNORE"
    echo "$OPENCODE_ENTRY" >> "$GITIGNORE"
    echo "✅ '$ENTRY', '$SETTINGS_ENTRY', '$MCP_CLAUDE_ENTRY', and '$OPENCODE_ENTRY' added to the existing .gitignore."
else
    # If the file does not exist, create a new one
    echo "$ENTRY" >> "$GITIGNORE"
    echo "$SETTINGS_ENTRY" >> "$GITIGNORE"
    echo "$MCP_CLAUDE_ENTRY" >> "$GITIGNORE"
    echo "$OPENCODE_ENTRY" >> "$GITIGNORE"
    echo "✅ New .gitignore created with entries '$ENTRY', '$SETTINGS_ENTRY', '$MCP_CLAUDE_ENTRY', and '$OPENCODE_ENTRY'."
fi

# 3. Create .mcp.json file
MCP_FILE=".mcp.json"
cat > "$MCP_FILE" << 'EOF'
{
    "mcpServers": {
    }
}
EOF
echo "✅ .mcp.json for claude code created successfully."

# 4. Create opencode.json file
OPENCODE_FILE="opencode.json"
cat > "$OPENCODE_FILE" << 'EOF'
{
  "mcp": {
  }
}
EOF
echo "✅ opencode.json created successfully."