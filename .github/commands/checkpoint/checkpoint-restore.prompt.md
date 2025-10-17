# /restore

Restore the project to a previous checkpoint state.

## Usage

```
/restore <checkpoint-id> [--force]
```

## Arguments

- `checkpoint-id` (required): The commit ID or short hash of the checkpoint to restore
- `--force` (optional): Force restore even if there are uncommitted changes

## Description

Restores the project to a previous checkpoint by performing a git reset. This command:
- Checks if the specified checkpoint exists
- Warns about uncommitted changes (unless --force is used)
- Resets the working directory to the checkpoint state
- Provides confirmation of the restore operation

## Configuration

```yaml
allowed-tools:
  - Bash
```

## Implementation

```bash
#!/bin/bash

# Check arguments
if [ $# -eq 0 ]; then
    echo "Error: Checkpoint ID is required."
    echo "Usage: /restore <checkpoint-id> [--force]"
    echo ""
    echo "Use /list-checkpoints to see available checkpoints."
    exit 1
fi

CHECKPOINT_ID="$1"
FORCE_FLAG="$2"

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "Error: Not in a git repository."
    exit 1
fi

# Verify the checkpoint exists
if ! git cat-file -e "$CHECKPOINT_ID" 2>/dev/null; then
    echo "Error: Checkpoint '$CHECKPOINT_ID' not found."
    echo ""
    echo "Use /list-checkpoints to see available checkpoints."
    exit 1
fi

# Check for uncommitted changes
if ! git diff --quiet || ! git diff --cached --quiet; then
    if [ "$FORCE_FLAG" != "--force" ]; then
        echo "Warning: You have uncommitted changes that will be lost."
        echo ""
        echo "Current changes:"
        git status --porcelain
        echo ""
        echo "To proceed anyway, use: /restore $CHECKPOINT_ID --force"
        echo "To save current changes first, use: /checkpoint \"Before restore\""
        exit 1
    fi
fi

# Get commit info for confirmation
COMMIT_MESSAGE=$(git log --format=%s -n 1 "$CHECKPOINT_ID")
COMMIT_DATE=$(git log --format=%cd -n 1 "$CHECKPOINT_ID")

echo "Restoring to checkpoint: $CHECKPOINT_ID"
echo "Message: $COMMIT_MESSAGE"
echo "Date: $COMMIT_DATE"
echo ""

# Perform the restore
git reset --hard "$CHECKPOINT_ID"

if [ $? -eq 0 ]; then
    # Clean untracked files
    git clean -fd

    echo "✓ Successfully restored to checkpoint $CHECKPOINT_ID"
    echo ""
    echo "Current HEAD is now at:"
    git log --oneline -1
else
    echo "Error: Failed to restore checkpoint."
    exit 1
fi
```