# Synchronization Script

This folder contains the script for bi-directionally synchronizing agent skills between the human-readable [Practice of Product](https://sean.horgan.net/Practice+of+Product/Practice+of+Product) Obsidian vault and the markdown files used for AI agents.

## How the Sync Works (`sync_skills.py`)

The `sync_skills.py` script ensures that the public site and agent skills remain in harmony.

To run a dry run (shows changes without saving):

```bash
python sync_skills.py --dry-run
```

To execute the sync:

```bash
python sync_skills.py
```

## Sync Rules & Conflict Resolution

1. **Source of Truth:** The script uses the file's Last Modified Time (`mtime`) to determine directionality.
   - Modifying a file in Obsidian overwrites the older version in the agent skills folder.
   - Modifying an agent skill directly overwrites the older version in Obsidian.
2. **Obsidian -> agent (Exporting):** Removes Obsidian-specific syntactic sugar. `[[WikiLinks]]` are converted to standard text or standard markdown links. Images `![[]]` are stripped if they cannot be rendered by standard LLMs.
3. **Agent Instructions Block:** The sync script automatically injects an `<agent_instructions>` XML block at the top of every synced file. This tells the LLM to follow the rubrics precisely, ensuring it adheres to Sean's specific frameworks over its own generic training data.
