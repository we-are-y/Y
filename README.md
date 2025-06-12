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

