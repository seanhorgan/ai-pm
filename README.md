# Agent Skills for Product Management

This repository contains agent instructions ("skills") that reflect Sean Horgan's Product Management philosophy, codified on his [Practice of Product](https://sean.horgan.net/Practice+of+Product/Practice+of+Product) site.

## The Strategy: Core Persona + Domain Skills

Instead of providing an AI agent with a massive "master document" (which dilutes its instruction following), we use a two-tier approach.

### 1. The Core Persona

- **File:** `~/.agent/workflows/product_os.md`
- **Usage:** Provide this to the agent for _almost every_ product management task. By placing it in `~/.agent/workflows/`, AntiGravity reads this file globally for every workspace on your Mac.
- **Content:** This contains the foundational principles that govern all product thinking (e.g., Wardley Mapping: Pioneers/Settlers/Town Planners, Kent Beck's 3X Explore/Expand/Extract framework, and general communication tone). It also contains a **Skills Index** which the agent uses to autonomously identify and read appropriate domain skills from the `~/.agent/workflows/product_skills/` folder.

### 2. Domain-Specific Skills

- **Location:** The `~/.agent/workflows/product_skills/` directory.
- **Usage:** Pull these in on-demand when working on specific tasks (e.g., leveling a PM, structuring an organization, or planning discovery sprints). Because they are in the agent workflows directory, AntiGravity has global access to them.
- **Content:** These are targeted markdown files synced directly from the "Practice of Product" Obsidian vault. They contain actionable rubrics and frameworks.

---

## Bi-Directional Synchronization with Obsidian

To maintain a single source of truth for the human-readable site while providing optimized, actionable instructions for AI agents, we utilize a bi-directional sync script.

### Where Content Lives

Sean's Practice of Product site is the source of truth for the human-readable site which you can find at https://sean.horgan.net/Practice+of+Product/Practice+of+Product. The agent skills are derived from the site and are stored globally in the `~/.agent/workflows/product_skills/` directory.

### How the Sync Works (`sync_skills.py`)

The `sync_skills.py` script ensures that your public site and your agent skills remain in harmony.

To run a dry run (shows changes without saving):

```bash
python sync_skills.py --dry-run
```

To execute the sync:

```bash
python sync_skills.py
```

### Sync Rules & Conflict Resolution

1. **Source of Truth:** The script uses the file's Last Modified Time (`mtime`) to determine directionality.
   - Modifying a file in Obsidian overwrites the older version in `~/.agent/workflows/product_skills`.
   - Modifying an agent skill in `~/.agent/workflows/product_skills` overwrites the older version in Obsidian.
2. **Obsidian -> agent (Exporting):** Removes Obsidian-specific syntactic sugar. `[[WikiLinks]]` are converted to standard text or standard markdown links. Images `![[]]` are stripped if they cannot be rendered by standard LLMs.
3. **Agent Instructions Block:** The sync script automatically injects an `<agent_instructions>` XML block at the top of every file in the `product_skills` directory. This tells the LLM to follow the rubrics precisely, ensuring it adheres to Sean's specific frameworks over its own generic training data.
