# 🌟 Y

## 🚀 Quick Links
- [Vault Documentation](vault/README.md)
- [Signal Layer Documentation](signal/README.md)
- [Echo Documentation](echo/README.md)
- [API Layer Documentation](api_layer/README.md)
- [Grid Documentation](grid/README.md)
- [MCP Documentation](mcp/README.md)

Y is a comprehensive system for personal data sovereignty, AI assistance, and value attribution in the digital age.

## 🧩 Schema Registry & Extensibility

Y uses a dynamic **schema registry** to support any data type, now and in the future. New data types can be described (fields, units, display names, UI hints, etc.) and registered without code changes. This ensures:
- The Vault, Echo, and dashboard adapt automatically
- Developers and users can extend the system with new data sources
- Backward compatibility via versioning

## 💸 Value Calculation & Vault Score

Y calculates the value of your Vault using a blend of:
- **Demand**: How many requests exist for this data type?
- **Rarity**: Is your data common or unique?
- **Completeness/Quality**: How detailed and well-structured is your data?
- **Freshness**: Is your data recent?
- **Signal Density**: Richness of behavioral/emotional/other signals
- **Streaks & Decay**: Consistent uploads are rewarded, outdated data loses value

Your **Vault Score** and earning potential are shown in the dashboard, along with tips to increase your value.

## 🏗 System Architecture

```
Y/
├── vault/                    # Human Vault system (UI, backend, schema)
│   ├── ui/                   # Frontend interface (React + Tailwind)
│   ├── backend/              # Supabase client, FastAPI routes, auth
│   ├── data_models/          # JSONSchemas or Supabase table formats
│   └── README.md
│
├── signal/                   # Signal Layer (data parsing, embeddings)
│   ├── processors/           # Spotify, Gmail, Rewind parsers etc.
│   ├── embeddings/           # OpenAI, custom transformers, vector code
│   ├── quality_scoring/      # Data quality logic + weights
│   └── README.md
│
├── echo/                     # Personal AI agent (Echo)
│   ├── memory/               # Persistent long-term memory
│   ├── prompts/              # Prompt templates and role behavior
│   ├── routing/              # Agent interaction and decision logic
│   └── README.md
│
├── api_layer/                # Human + Enterprise API logic
│   ├── access_control/       # Gatekeeper agents, consent logic
│   ├── monetization/         # Royalties, usage tracking, payouts
│   └── README.md
│
├── grid/                     # Value-routing and agent execution layer
│   ├── compute/              # Agent execution infra
│   ├── dividend_engine/      # Attribution + dividend routing logic
│   └── README.md
│
├── mcp/                      # Model Context Protocol orchestrator
│   ├── agents/               # System-level MCP actors
│   ├── flows/                # .yaml or .json workflows, diagrams
│   └── README.md
│
├── tests/                    # Test cases for each component
│
├── .env                      # Secrets and keys (gitignored)
├── requirements.txt          # Python deps
├── package.json              # JS deps (for UI)
├── docker-compose.yml        # Optional: for unified local dev
└── README.md                 # This file
```

## 🚀 Getting Started

1. Clone the repository:
```bash
git clone https://github.com/yourusername/y.git
cd y
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your credentials
```

3. Install dependencies:
```bash
# Python dependencies
pip install -r requirements.txt

# JavaScript dependencies
npm install
```

4. Start the development environment:
```bash
docker-compose up
```

## 🎯 Key Features

- **Data Sovereignty**: Complete control over your personal data
- **AI Assistance**: Personalized AI agent that grows with you
- **Value Attribution**: Fair compensation for data contributions
- **Privacy First**: End-to-end encryption and zero-knowledge proofs
- **Enterprise Ready**: Business-grade APIs and integrations

## 🛠 Technology Stack

- **Frontend**: React, Next.js, TailwindCSS
- **Backend**: FastAPI, Supabase
- **AI/ML**: OpenAI, Custom Transformers
- **Database**: PostgreSQL, Vector Storage
- **Infrastructure**: Docker, Kubernetes

## 📚 Documentation

Each component has its own detailed documentation:

- [Vault Documentation](vault/README.md)
- [Signal Layer Documentation](signal/README.md)
- [Echo Documentation](echo/README.md)
- [API Layer Documentation](api_layer/README.md)
- [Grid Documentation](grid/README.md)
- [MCP Documentation](mcp/README.md)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

## 📄 License

MIT

## 🙏 Acknowledgments

- OpenAI for their groundbreaking work in AI
- The open-source community for their invaluable contributions
- All the early adopters and contributors to the Y project

# 🧬 Y: The Sovereign Interface

**Y is not a product. Y is a direction.**  
A living infrastructure where human beings reclaim ownership of their data, agency over their intelligence, and value from their existence.

---

## ❓ What Is Y?

Y is a sovereign operating layer — not for your computer, but for your **self**.

It is the system that:
- Stores your life securely (Vault)
- Understands your behaviors (Signal Layer)
- Negotiates access and value (Human & Enterprise API)
- Routes dividends from your contributions (Grid)

Y flips the current data economy:
> From platforms owning people —  
> To people owning the platforms.

---

## 🧠 Why Y Exists

We are approaching the **post-labor world** —  
A future where AI, robotics, and automation will replace almost every job humans do today.

In that world, your signal is more valuable than your labor.

But today:
- Humans are reduced to data points.
- Privacy is performative.
- AI systems scale on human input — without recognition or compensation.

**Y exists to change that.**  
To make sure humans don't just survive in the age of AI — they **thrive**.

---

## 💡 What Makes Y Different?

- ❌ Y is **not** a marketplace
- ❌ Y is **not** a collection of bots
- ❌ Y is **not** a passive data vault

- ✅ Y is a **sovereign system**
- ✅ Y is an **intentional architecture for human dignity**
- ✅ Y is a **living interface between self, signal, and society**

It is a radical reframing of value —  
Where your *existence* is enough to earn.  
Where your *consent* is real.  
Where your *Vault* is the beginning of everything.

---

## 🧱 Core Components

| Component        | Purpose |
|------------------|---------|
| `vault/`         | Your encrypted, intelligent life record |
| `signal/`        | AI that learns from you, not about you |
| `api/`           | Consent-based access to your data |
| `grid/`          | Monetization + attribution engine |
| `echo/`          | Your intelligent reflection and sovereign agent |
| `mcp/`           | Model Context Protocol — ensures all AI agents interact with your data on your terms |
| `docs/`          | Living documentation of the Y system |

---

## 🧭 Our Founding Thesis

> If the future makes us unnecessary as workers,  
> Then Y makes us **sacred as people**.

Y doesn't optimize for systems.  
Y optimizes for the **soul**.

---

## 🌍 What Happens Here

This repository is the **central monorepo** of Y.  
We use it to build, document, and evolve every part of the system.

You'll find:
- Specs
- Architecture
- Agents
- Vault schemas
- API protocols
- Build notes
- Research threads

This is where **human sovereignty becomes code**.

---

## 🛠 Contributing

Currently, development is limited to the founding team.  
Want to help? Start by understanding the [Vault architecture](./vault/) and [Echo design](./echo/), and submit a proposal via `issues`.

---

## 🙏 A Note From the Founder

Y was born out of a deep belief:

That when the world stops needing us to work —  
we must build a world where we are still needed.  
Not as cogs. But as whole, sovereign humans.

Thank you for being here. We're building the long game.

—

## 📚 Glossary
- **Schema Registry**: A dynamic table describing all supported data types, fields, and UI hints
- **Vault Score**: A metric estimating the value of your data based on demand, quality, and other factors
- **Echo**: Your personal AI agent, powered by your Vault
- **Signal Layer**: The system that processes raw data into structured, valuable signals
- **Grid**: The value-routing and attribution engine
- **MCP**: Model Context Protocol, orchestrating context and memory for all agents

## 🧩 Building on Y: Vault-Native Modules, Not Standalone Apps

Y is not a generic developer platform for launching new apps. Instead, Y is a protocol and interface for building Vault-native modules—tools, dashboards, agents, and plugins that run inside the Vault, the user's trusted home and operating system for their data and intelligence.

**If you're building on Y, you're building for the Vault.**

- All modules run inside the Vault interface
- All modules follow Y's data standards and schema
- All modules respect consent and value-routing protocols
- All modules are reviewed, authenticated, and optionally monetized through Y

**You do not build standalone apps. You build Vault-native modules.**

### Examples of Vault-Native Modules
- Dashboards that visualize health, habits, or learning
- AI agents trained on Vault signal
- Research request layers (with user consent)
- Simulation tools, coaching layers, family views
- Plugins that extend Echo's capabilities

### For Developers: How to Build a Vault-Native Module
1. Register your module with the Vault, specifying its schema, permissions, and UI integration points.
2. Use Y's APIs and schema registry to access and process user data (with consent).
3. Ensure your module respects all consent, value-routing, and privacy protocols.
4. Submit your module for review and authentication.
5. Optionally, monetize your module through Y's value-routing engine.

**All modules are always under user control: visible, revocable, and permissioned.**

## 🧩 Examples of Vault-Native Modules

All modules, dashboards, and agents below are built for the Vault — not as standalone apps. They are delivered through Y's protocol, surfaced in your interface, and governed by user consent.

⸻

🧠 1. Dashboards & Insights Modules
Custom lenses for viewing and interpreting Vault signal.
    • Sleep + Recovery Tracker
    • Emotional Resilience Map
    • Focus vs. Distraction Loops
    • Financial Behavior Explorer
    • Parenting Stress Signals
    • Language & Voice Shift Visualizer
    • Productivity x Circadian Map

🧩 Delivered via: Vault Interface → "Insights" or "Dashboards"

⸻

🤖 2. Echo Plugins & Personal AI Agents
Intelligent agents trained on Vault data or extending Echo's abilities.
    • Mental Health Companion
    • Learning Coach
    • Fitness & Diet Optimizer
    • Memory Recall Assistant
    • Creative Idea Generator
    • Social Pattern Analyzer
    • Goal Accountability Agent

🧩 Delivered via: Vault Interface → "Echo" or "Agent Hub"

⸻

🔬 3. Research & Compliance Modules
Enterprise dashboards or tools that access Vault data via consent.
    • Study Participation Request Panels
    • Clinical Trial Qualification Interfaces
    • Health Signal Collection Tools
    • Compliance/Audit Reporting Modules
    • Open Science Contribution Tools

🧩 Delivered via: Vault Interface → "Requests" or "External Access"
🛠 Powered by: Enterprise API

⸻

💸 4. Data Monetization Modules
Interfaces that support value exchange directly within the Vault.
    • Signal Licensing Offers
    • Insight-for-Credit Exchanges
    • Agent Pack Store
    • Donation Pools for Causes/Research
    • Micro-Marketplace Interfaces (e.g. for niche data types)

🧩 Delivered via: Vault Interface → "Earnings" or "Vault Store"

⸻

👥 5. Family & Group Interfaces
Modules designed for shared use cases across multiple Vaults.
    • Shared Health Dashboards
    • Parent-Child Learning Tracker
    • Elder Care Monitoring
    • Consent Delegation Interfaces
    • Family Planning Signal Maps

🧩 Delivered via: Vault Interface → "Shared Vaults"

⸻

🧰 6. Developer Tools
Power-user or builder tools that help manage or extend Vaults.
    • CLI Tools (query, export, simulate)
    • Custom Data Injection Scripts
    • Local Agent Test Environments
    • Vault Snapshot Generators
    • Dev SDKs for Python/JS

🧩 Delivered via: "Dev Tools" tab or through secure local environments

⸻

🧩 The Golden Rule:

All of these are Vault-native modules, not standalone apps.
They plug into Y's schema, follow the consent + value protocol, and are surfaced inside your interface — not theirs.

---

## ❓ Protocol vs. Product: What's the Difference?

- **Product:** A finished application or service for end users. (e.g., the Vault app itself)
- **Protocol:** The open rules, APIs, and standards that define how modules interact with data, value, and consent—inside the Vault.

**Y is a protocol and interface. The Vault is the one app that matters. Everything else is a module that lives inside it.**

---

