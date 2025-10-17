# /list-checkpoints

List all available checkpoints in the repository.

## Usage

```
/list-checkpoints [--limit=N]
```

## Arguments

- `--limit=N` (optional): Limit the number of checkpoints to display (default: 20)

## Description

Displays a list of all checkpoint commits in the repository, showing:
- Short commit hash (checkpoint ID)
- Commit message
- Author and date
- Relative time

Only shows commits with "CHECKPOINT:" prefix for easy identification.

## Configuration

```yaml
allowed-tools:
  - Bash
```

## Implementation

```bash
#!/bin/bash

# Default limit
LIMIT=20

# Parse arguments
for arg in "$@"; do
    case $arg in
        --limit=*)
            LIMIT="${arg#*=}"
            ;;
        *)
            echo "Unknown argument: $arg"
            echo "Usage: /list-checkpoints [--limit=N]"
            exit 1
            ;;
    esac
done

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "Error: Not in a git repository."
    exit 1
fi

# Get checkpoint commits
echo "📋 Available Checkpoints (limit: $LIMIT)"
echo "========================================"
echo ""

# Check if there are any checkpoint commits
CHECKPOINT_COUNT=$(git log --oneline --grep="^CHECKPOINT:" --all | wc -l)

if [ "$CHECKPOINT_COUNT" -eq 0 ]; then
    echo "No checkpoints found."
    echo ""
    echo "Create your first checkpoint with: /checkpoint \"Your message\""
    exit 0
fi

# Display checkpoints in a nice format
git log \
    --grep="^CHECKPOINT:" \
    --all \
    --pretty=format:"%C(yellow)%h%C(reset) %C(green)%cr%C(reset) %C(blue)%an%C(reset)%n  %s%n" \
    -n "$LIMIT"

echo ""
echo "──────────────────────────────────────────"
echo "Found $CHECKPOINT_COUNT checkpoint(s) total"
echo ""
echo "To restore a checkpoint: /restore <checkpoint-id>"
echo "To create a new checkpoint: /checkpoint [message]"
```