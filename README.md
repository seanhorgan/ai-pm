# Agent Skills for Product Management

This repository contains AI agent instructions ("skills") that reflect core Product Management philosophies. It is designed as a standalone guide that can be easily adopted by product leaders to scale their team's effectiveness using AI. The core concepts are codified from the [Practice of Product](https://sean.horgan.net/Practice+of+Product/Practice+of+Product) site.

## The Strategy: Core Persona + Domain Skills

Instead of providing an AI agent with a massive "master document" (which dilutes its instruction following), we use a modular, two-tier approach.

### 1. The Core Persona

The foundation for all agent interactions.

- **Usage:** Provide this to the agent for _almost every_ product management task. 
- **Content:** This contains the foundational principles that govern all product thinking (e.g., Wardley Mapping: Pioneers/Settlers/Town Planners, Kent Beck's 3X Explore/Expand/Extract framework, and general communication tone). It also contains a **Skills Index** which the agent uses to autonomously identify and read appropriate domain skills when needed.

### 2. Domain-Specific Skills

Focused playbooks for specialized work.

- **Location:** The `skills/` directory in this repository.
- **Usage:** Pull these in on-demand when working on specific tasks (e.g., leveling a PM, structuring an organization, or planning discovery sprints). 
- **Content:** These are targeted markdown files containing actionable rubrics and frameworks.

---

## How to Use These Skills (For Others)

If you want to use these PM skills (like the `Product Discovery.md` framework) in your own AI agent environment, you can seamlessly integrate them into your workflow:

### 1. Antigravity Integration
If you use [Antigravity](https://github.com/google/antigravity) or another Model Context Protocol (MCP) compatible agent, expose these skills globally by adding the local filesystem server to your configuration.
*   **Via MCP Config:** Copy the provided `mcp_config.example.json` to your `~/.gemini/antigravity/mcp_config.json` (or equivalent location), replacing the path with the absolute path to your cloned `ai-pm/skills` directory. 
*   **Via Symlink:** Alternatively, you can symlink the cloned skills directly into your project: `ln -s /path/to/ai-pm/skills .agent/skills`

### 2. Cursor Integration
If you use Cursor IDE, easily reference these skills when prompting.
*   **Prompt Referencing:** Mention `@skills/Product Discovery.md` in the chat or composer when you want the AI to follow that specific rubric.
*   **Global Rules:** You can copy the `<agent_instructions>` block and the relevant domain frameworks from these files directly into your project's `.cursorrules` file if you want them always active.

### 3. Claude.ai / ChatGPT Integration
For web-based LLMs, upload these markdown files to give the model persistent knowledge of these PM frameworks.
*   **Claude Projects:** Upload the `.md` files to the "Knowledge" section of a Claude Project.
*   **Custom GPTs:** Upload the files to the "Knowledge" section when configuring a custom GPT in OpenAI. 

*(**Note on OpenSpec Compatibility:** Many of the skills generated here, such as the Product Discovery skill, are designed to synthesize their outputs into standardized formats like those laid out by [OpenSpec](https://github.com/Fission-AI/OpenSpec).)*
