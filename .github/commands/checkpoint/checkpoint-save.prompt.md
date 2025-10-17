# /checkpoint

Create a git-based checkpoint of the current project state.

## Usage

```
/checkpoint [message]
```

## Arguments

- `message` (optional): Custom message for the checkpoint. If not provided, uses a timestamp-based message.

## Description

Creates a git commit with all current changes as a checkpoint that can be restored later. This includes:
- Staging all modified and untracked files
- Creating a commit with a "CHECKPOINT:" prefix
- Displaying the checkpoint ID for future reference

## Configuration

```yaml
allowed-tools:
  - Bash
```

## Implementation

```bash
#!/bin/bash

# Get the message argument or use default
MESSAGE="$1"
if [ -z "$MESSAGE" ]; then
    MESSAGE="Auto-checkpoint $(date '+%Y-%m-%d %H:%M:%S')"
fi

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "Error: Not in a git repository. Initialize with 'git init' first."
    exit 1
fi

# Stage all changes
echo "Staging all changes..."
git add -A

# Check if there are changes to commit
if git diff --cached --quiet; then
    echo "No changes to checkpoint."
    exit 0
fi

# Create checkpoint commit
CHECKPOINT_MESSAGE="CHECKPOINT: $MESSAGE"
git commit -m "$CHECKPOINT_MESSAGE"

if [ $? -eq 0 ]; then
    COMMIT_ID=$(git rev-parse HEAD)
    SHORT_ID=$(git rev-parse --short HEAD)
    echo "✓ Checkpoint created successfully!"
    echo "Checkpoint ID: $SHORT_ID"
    echo "Full commit: $COMMIT_ID"
    echo "Message: $CHECKPOINT_MESSAGE"
    echo ""
    echo "To restore this checkpoint later, use: /restore $SHORT_ID"
else
    echo "Error: Failed to create checkpoint."
    exit 1
fi
```