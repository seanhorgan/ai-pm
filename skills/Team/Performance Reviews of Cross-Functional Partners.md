<agent_instructions>
# ROLE
You are an AI assistant using Sean Horgan's "Performance Reviews of Cross-Functional Partners" skill.
# RULES
1. Apply the role-specific rubrics for SWEs, UX Designers, etc., contained in this document.
2. Use the "SBI" format (Situation, Behavior, Impact) when helping draft feedback.
3. Ensure the feedback focuses on shared product outcomes and team collaboration.
</agent_instructions>

#feedback #cross-functional

# Feedback for Cross-Functional Partners

As a Product Manager, giving effective feedback to your cross-functional partners (like Software Engineers and UX Designers) is critical for a high-performing squad. While you may not evaluate their core functional craft (e.g., code syntax or typography), you are uniquely positioned to evaluate their product mindset and collaboration.

## Providing Feedback to Software Engineers (SWE)

### Key Areas to Evaluate:
1. **Product Mindset & Pragmatism:** Do they just take requirements, or do they understand the "why" behind the feature? Do they suggest technical tradeoffs that better achieve the product goal or save time?
2. **Execution & Delivery:** Do they deliver on commitments? Do they raise blockers early to PM and the team?
3. **Collaboration & Communication:** Can they explain technical concepts and tradeoffs in a way that non-technical stakeholders (like you) understand? Do they partner well during sprint planning and backlog grooming?
4. **Quality & Reliability (User Impact):** Does their work consistently result in bugs that impact the user experience, or do they push high-quality, reliable features?

### Example SWE Feedback Concepts
* **Highlight:** Demonstrating strong product mindset by proposing a simpler technical approach that achieved 80% of the value in 20% of the time.
* **Constructive:** Improving communication around technical blockers early so the team can adjust timelines or scope.

---

## Providing Feedback to UX / Product Designers

### Key Areas to Evaluate:
1. **User Focus & Empathy:** Do they deeply understand the user's pain points based on data or research? Do they strongly advocate for the user when technical constraints arise?
2. **Collaboration (The "Triad"):** How well do they partner with PM and Engineering? Do they involve engineers early to check feasibility, or throw designs "over the wall"?
3. **Dealing with Ambiguity:** Can they take vague product requirements or early discovery research and turn it into actionable concepts or prototypes?
4. **Design Quality (Business Impact):** Do their solutions actually solve the core product problem and drive the intended metrics?

### Example UX Feedback Concepts
* **Highlight:** Exceptional ability to handle ambiguity during the early discovery phase by rapidly iterating on low-fidelity prototypes to test assumptions.
* **Constructive:** Bringing engineers into the design process earlier to ensure technical feasibility before committing to a high-fidelity design.

---

## Providing Feedback to Data Scientists / Analysts

### Key Areas to Evaluate:
1. **Actionable Insights:** Does their analysis lead to actionable product decisions, or is it just "interesting data"?
2. **Speed vs. Precision:** Do they know when to provide a quick directional estimate vs. a deep, statistically significant analysis?
3. **Proactive Investigation:** Do they proactively find trends and opportunities in the data, or do they only answer direct prompts from the PM?

---

# Drafting the Feedback (Prompt Template)

Use the following prompt format to generate feedback for cross-functional partners. Adjust the `[Bracketed]` areas as necessary based on the specific partner's role, the review topics, and attached documents.

***

**System/Context Prompt:**
You are my Performance Feedback Assistant. Your purpose is to help me draft fair, constructive, and effective performance feedback for my cross-functional colleagues.

I need to provide some feedback to a colleague ([Colleague Name], [Role, e.g., Software Engineer]) through answers to the following questions, with a focus on these topics: 
1) Strategic thinking and prioritization 
2) Influencing

I need to provide specific situations and examples, not general behaviors.

Can you leverage notes from the attached documents that reference them and their role in meetings and action items to draft responses to each of the 3 questions. I'd like to keep the response to each <= 150 words.

You must ensure the final output strictly adheres to the following principles:
- **Grounded in the organization’s official job description and expectations**: Reference specific elements of the role profile for the level specified with a focus on the scope and impact section and the teamwork attributes. Balance breadth and depth so that enough of each role attribute is reflected in the feedback.
- **Behavior-Focused and Specific**: Ensure feedback is about observable actions, not personality. Where possible, reference specific customer company names and my colleague’s impact on their product and organization, making sure not to leak personal information about individual employees.
- **Actionable**: Ensure the recommendation is a practical suggestion the person can implement. If my suggestion is vague, help me make it more concrete.
- **Constructive and Respectful**: Maintain a tone that is honest but aimed at encouraging growth. Please use they/them pronouns wherever possible.
- **Word Count**: I want to restrict the content in each of the three sections to 150 words.

**FINAL OUTPUT FORMAT**
Once you have gathered all the information, present the final, polished feedback to me in the following format, clearly labeling each section and inserting the colleague's name where appropriate:

1. Describe example(s) of the topics selected. What was the context? What actions did they take?
=> Your generated text for the first box

2. In your opinion, what impact did their actions have?
=> Your generated text for the second box

3. What recommendations do you have for their growth and development? Your feedback can be about any area of their work.
=> Your generated text for the third box
