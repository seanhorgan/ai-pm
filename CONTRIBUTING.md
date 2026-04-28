# Contributing

This repo is the public, AI-optimized version of a private Obsidian vault. Contributions are welcome — especially improvements to skill content, new skills, and sync tooling.

## How to contribute

1. Fork the repo and create a feature branch.
2. Make your changes. If editing a skill file, follow the existing format: `When to use` → `Rubric/Principles` → `Actions`.
3. If you modify `sync/sync_skills.py`, add or update tests in `sync/test_sync_skills.py`.
4. Open a pull request with a clear description of what you changed and why.

## Skill file conventions

- Each skill file lives in `skills/` as a standalone `.md` file.
- Do NOT add `<agent_instructions>` blocks manually — the sync script injects these.
- Use standard markdown. Avoid Obsidian-specific syntax (`[[wiki-links]]`, `![[embeds]]`) in the published files.

## Questions?

Open an issue or reach out to [@seanhorgan](https://github.com/seanhorgan).
