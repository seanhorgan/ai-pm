# Agent Skills for Product Management

AI agent instructions ("skills") that reflect core Product Management philosophies, codified from the [Practice of Product](https://sean.horgan.net/Practice+of+Product/Practice+of+Product) framework.

## Architecture

```
AGENTS.md              ← Universal AI entry point (start here)
skills/                ← 14 distilled, AI-executable playbooks
sync/                  ← Sync tooling for Obsidian vault ↔ repo
```

**`AGENTS.md`** is the entry point for any AI system. It establishes the PM persona, indexes all skills, and explains how to use them. Point your agent here first.

**`skills/`** contains focused, imperative playbooks (20–60 lines each) designed for AI execution — not lengthy essays. Each skill has: when to use it, rubrics/principles, and specific actions the AI should take.

### Skills Index

| Skill | Use when |
|-------|----------|
| Core PM Persona | Foundation for all PM work — load first |
| PM Levels & Expectations | Leveling, career ladder, calibration |
| Leadership | Coaching leadership, team dynamics |
| Strategic Thinking | Strategy writing, competitive analysis |
| Product & Design | Discovery, prioritization, PMF |
| Analytical Thinking | Metrics, structured problem solving |
| Communication | Presentations, stakeholder alignment |
| Entrepreneurship | 0→1 products, GTM, pricing |
| Culture | Team health, organizational values |
| Strategy Brief | Writing/reviewing strategy documents |
| PM Ownership | Scope-setting, doc templates, onboarding |
| Building a PM Team | Org design, hiring, managing PMs |
| Performance Reviews | Writing reviews, feedback, calibration |
| Partner Evaluation | Partner company assessment using PACT rubric |

---

## How to Use These Skills

### AGENTS.md auto-discovery (Claude Code, OpenAI Codex, Cursor)
Clone this repo into your project. These tools auto-discover `AGENTS.md` at the project root — no configuration needed.

### MCP filesystem server
Expose the skills directory to any MCP-compatible agent. Copy `mcp_config.example.json` to your agent's config, replacing the path with your local clone:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/ai-pm/skills"]
    }
  }
}
```

### Claude Projects / Gemini / ChatGPT
Upload `AGENTS.md` plus the relevant skill files to the knowledge or system prompt section.

### Cursor IDE
Reference skills inline: `@skills/Product Discovery.md`. Or embed `AGENTS.md` in your `.cursorrules` file.

---

## Source of Truth

These skills are distilled from a private Obsidian vault. The vault contains rich, human-readable essays under `Practice of Product/`; the `skills/` files here are the AI-optimized versions. The `sync/` directory contains tooling for keeping the two in sync.
