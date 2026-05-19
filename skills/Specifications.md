# Skill: Writing Product Specifications for AI Infrastructure & Platform Workloads

This skill defines the template and standard elements required when writing a Product Requirements Document (PRD) or Specification for AI infrastructure, serving platforms, or orchestration systems (e.g., agent serving frameworks, KV-caching fabrics). 

Infrastructure specifications differ significantly from application specifications (e.g., mobile apps) because they focus on resource constraints, hardware-software co-design, and system orchestration.

---

## 1. Required Specification Elements

Every AI Infrastructure/Platform specification should include the following core sections:

### 1.1. Why This Work is Important (Core Vision)
*   **Format**: Maximum 3 sentences.
*   **Focus**: Clearly define the paradigm shift in the workload (e.g., transition from one-shot chat to multi-turn agent loops; compute-bound to memory-bound constraints) and the business threat or platform efficiency opportunity.

### 1.2. Success & Business Metrics
Identify both business and technical performance indicators:
*   **Business Impact**: Cost per completed task/session, Total Cost of Ownership (TCO) reduction, accelerator (GPU/TPU) resource utilization gains.
*   **Technical Performance**: Time-to-First-Token (TTFT) reduction, token-per-second throughput increases, zero-recompute cache hit rates.
*   **Measurement**: Specify exactly *how* these will be measured (e.g., trace replays, benchmarks, synthetic traffic simulators).

### 1.3. Personas & Critical User Journeys (CUJs)
Focus on the developer and operator persona:
*   **Developer Persona (App Builder)**: Needs simple APIs, low loop latency, and predictable costs without managing hardware details.
*   **Platform Engineer Persona (Cluster Operator)**: Needs high utilization, multi-tenant fairness, cost allocation tracking, and automated scaling.
*   **Critical User Journeys**: Must specify multi-step systems behaviors:
    *   *Branching execution paths* (e.g., Tree-of-Thought search).
    *   *State pauses* (e.g., agent calls a tool and pauses, requiring cache offloading).
    *   *Multi-tenant resource sharing* (e.g., batch jobs vs. interactive tasks).

### 1.4. Build vs. Leverage Matrix (The Ownership boundary)
For modular platform projects, explicitly define the boundary of responsibility. Use a table mapping:
*   **Component**: (e.g., Inference engine, Ingress gateway, custom scheduling plugin, secure sandbox runtime).
*   **Build vs. Leverage**: State whether you are writing this from scratch (**Build**) or using existing open-source/third-party systems (**Leverage**).
*   **Primary Owner**: The internal team or community group owning the code.
*   **Target Integration**: The connection point (e.g., engine transfer API, network gateway definitions).

### 1.5. Architectural Bundles ("Well-Lit Paths")
Instead of exposing raw infrastructure choices, define structured **Crawl-Walk-Run** deployment blueprints to guide customers:
*   **Crawl/Walk (Available Today)**: Use existing, stable, out-of-the-box components (e.g., Open Engine + Host Memory Caching + POSIX Storage mount) to deliver immediate latency/cost benefits.
*   **Run (Future)**: Transition to high-performance, custom hardware-integrated fabrics (e.g., Direct Device-to-Storage paths + RDMA high-speed memory fabric + distributed flash nodes).

### 1.6. Deployment & Integration Recipes
Include a concrete, step-by-step developer guide on how to stitch the "Well-Lit Path" components together:
*   Provide sample infrastructure configuration manifests (mounting storage volumes, setting engine-specific CLI flags, configuring environment variables).
*   Document known hardware constraints (e.g., host-to-device memory ratios) and software limitations (e.g., model-specific attention layer constraints).

### 1.7. Reference Library & Prioritization Matrix
Synthesize all related documents, competitor guides, and research:
*   **Reference Index Table**: List each document with location, category, key insights, and project relevance.
*   **Urgent vs. Important Matrix**: Structure the engineering roadmap using a 2x2 grid (where "Urgent" represents the next 3 months). Map work items directly to customer targets or specific system bottlenecks.