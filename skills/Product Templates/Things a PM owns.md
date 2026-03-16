<agent_instructions>
# ROLE
You are an AI assistant using Sean Horgan's "Things a PM owns" skill.
# RULES
1. Apply the frameworks and rubrics contained in this document precisely.
2. If this document contains a template, ensure your output matches its structure.
3. Adhere to Sean's core PM philosophy: focus on outcomes, avoid fluff, and consider the product's lifecycle stage (Explore/Expand/Extract).
</agent_instructions>

PMs are responsible for capturing ideas and turning them into results which usually requires writing docs that synthesize the work, align the team, and connect with users & customers.

Common across all docs should be the following sections/headers:

1. Objective
2. Risks
3. FAQ - start dropping any open questions here along with answers as you figure it out
4. Status & Meeting Notes 

## Product Requirements / Launch Docs
While I don’t love traditional PRDs for many many reasons, some orgs love these documents because they aspire to be the single source of truth & alignment for everything related to the product. Generally this is a set up for failure as most people are looking for different things and a single doc gets too cluttered and unmanageable. Having said that, there are times and places for making changes to templates and you should account for the work to make those changes.

**Philosophical Note: The format is the problem.** As outlined in ["There Is No PRD"](https://momentalos.com/blog/there-is-no-prd/), traditional PRDs force PMs to compress a complex web of context (customer signals, strategic goals, technical constraints) into a lossy, linear narrative that goes stale almost immediately. In the era of AI agents and rapid execution, narrative documents break down. Instead of monolithic PRDs, PMs should focus on capturing product intent as **atomic, interconnected, and queryable pieces of structured context**—the specific *why* behind a constraint or the exact rationale behind a decision. Ensure context is delivered in the format the consumer (human or AI) needs it.

**Context Integrity is Critical:** Furthermore, as discussed in ["From GitHub for Product Management — to Something Bigger"](https://momentalos.com/blog/from-github-for-product-management-to-something-bigger/), dumping contradictory documents or stale assumptions onto agents leads to confidently wrong outputs. Product knowledge requires a "GitHub for Product Management" approach: it must be versioned, traceable, and honest. Conflict resolution (flagging when a new decision contradicts a past assumption) is a first-class necessity to ensure agents and humans reason from truth, not just accumulated artifacts.

I’ve found Ash Maurya’s Lean Stack to be an enduring model for product discovery & development: [https://leanstack.com/](https://leanstack.com/). This model includes the following elements that should be included in every product brief: 

- Vision. This is a **succinct & simple** statement that describes the future state of your product. Why should it exist?
- Product: problem, solution, key metrics, cost structures
- Market: landscape w/customers & competitors, unfair advantage, channels, revenue streams
- Unique value proposition
- Plan/timeline to win. Usually best to lay out a series of milestones (e.g. M1, M2, etc) that start the learning process with live users ASAP.
- Risks & mitigation

Doc template

1. TLDR / Executive Summary
2. Approval / LGTM table
3. Go-To-Market
4. Appendix
   5. People & References

## 1:1s & team checkins
For 1:1s and team check-ins, I use the following structure
- People - always start with topics related to people. Sets the right tone with the team that they are the most important topic and you can frame this as action oriented
- Pipeline (customers)
- Product
- Partners
- Planning

## Pro Forma P&L

Even if your product serves the needs of internal users it’s good practice to maintain a P&L statement. This doesn’t need to pass SEC tests, just a simple accounting for revenue, costs that help you answer important product questions like your team’s marginal contribution to the overall company business.

## Team Basics & Rituals (The "House in Order")

Inspired by John Cutler's [TBM 12/52: The Basics](https://cutlefish.substack.com/p/tbm-1252-the-basics), PMs should ensure their team has the following connective tissue and operating rhythms established:

- **Charter and Mission:** Have a team charter and a team mission. Know whose life you're making easier and your operating principles.
- **Strategy & Models:** Connective tissue between strategy and roadmap. Utilize appropriate models to figure out inputs before bets.
- **Roadmap & Bets:** An always up-to-date, one-year, suitably detailed roadmap filled with Bets (not just rigid features).
- **Bet Artifacts:** Every bet should have a one-pager, a research folder, and a learning backlog. Avoid massive monolithic PRDs for work far off in the future.
- **Bet Metrics & Target Inputs:** Define metrics unique to the bet to understand usage, and ensure the bet targets persistent input metrics that stay stable over time.
- **Goals:** Establish either bet-specific goals or quarterly OKRs, making goal-setting safe but effective.
- **Rituals:** 
  - **Kickoffs:** Well-facilitated kickoffs for every bet.
  - **Learning Reviews:** Post-bet analysis of impact and key lessons.
  - **Retrospectives & Continuous Improvement:** Regular reflections on how things are going and small improvement experiments.