Agent Skill: Metrics Generator

Description: This skill analyzes Product Requirements Documents (PRDs), Strategy
Memos, or Project Plans to extract, synthesize, and define holistic success
metrics. It ensures that success is measured not just by product usage, but by
commercial impact, ecosystem growth, and brand positioning.

Trigger: Activate this skill when a user provides a project document and asks:
"Define success metrics," "How should we measure success?" or "What are our
KPIs?"

# 🧠 Core Principles for the Agent

When generating metrics, the agent must adhere to the C.U.B.E. Framework. Every
project requires a balanced scorecard across these four structural pillars:

1.  Commercial: How does this drive revenue, infrastructure consumption, or
    operational cost savings?
2.  User: Are the target personas actually using the core features, and is the
    product reducing their friction?
3.  Brand: Is this project successfully shifting the industry conversation,
    countering competitor narratives, or establishing thought leadership?
4.  Ecosystem: (If applicable) Is the open-source community, third-party vendor
    space, or partner network adopting, contributing to, or standardizing around
    this project?

⚙️ Execution Steps (Agent Instructions):

Step 1: Document Analysis & Extraction

  - Scan the provided text for explicit goals (e.g., "Our goal is to...", "We
    will measure success by...").
  - Identify the target audience (e.g., enterprise IT, open-source developers,
    financial analysts).
  - Identify the strategic threat or market context (e.g., "Competitors are
    locking users into proprietary ecosystems").

Step 2: Draft Categorized Metrics Generate 2-3 specific, measurable metrics for
each of the four C.U.B.E. pillars.

  - Guideline: Metrics must be actionable. Instead of "good user experience,"
    use "conversion rate from viewing the dashboard to deploying the artifact."

Step 3: Distill to the "Executive Summary" If the user asks for a simple or
concise list, select the single most impactful metric from each of the four
categories and present them in a clean, four-bullet list formatted to the
C.U.B.E. structure.

# 📊 General Examples (For Agent Reference):

1. Commercial (Impact & Revenue)

  - Example A: Attributed cloud compute revenue generated from workloads
    deployed directly via the new tool.
  - Example B: Reduction in pre-sales engineering hours spent on custom Proof of
    Concepts (POCs).
  - Example C: Percentage shift in customer deployments from highly constrained
    legacy hardware to newly available, cost-effective hardware.

2. User (Engagement & Adoption)

  - Example A: Number of distinct enterprise organizations (MAUs) actively
    analyzing data within the platform.
  - Example B: Conversion rate of users who transition from "viewing a
    configuration" to clicking "Deploy to Production."
  - Example C: Adoption rate of specific advanced features (e.g., filtering by
    advanced architectural configurations).

3. Brand (Market Narrative & Positioning)

  - Example A: Number of industry citations where the project's data is
    referenced by Tier-1 analysts or media to counter proprietary competitor
    claims.
  - Example B: Share of voice (SOV) regarding "open ecosystem performance" in
    target industry publications.
  - Example C: Percentage of published benchmarks that reflect "real-world,
    multi-node workloads" vs. legacy static tests.

4. Ecosystem (OSS & Community Growth)

  - Example A: Volume of verified third-party data contributions submitted to
    the unified open-source repository.
  - Example B: Number of distinct open-source projects or partners adopting the
    project's new unified schema/standard.
  - Example C: Number of external feature developers utilizing the platform's
    automation for continuous regression testing.
