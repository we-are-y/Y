# 📊 Grid

The Grid is the value-routing and agent execution layer that powers the Y system.

## Components

### Compute
- Agent execution infrastructure
- Resource allocation
- Load balancing
- Performance monitoring
- Scaling management

### Dividend Engine
- Value attribution
- Dividend calculation
- Payment routing
- Usage tracking
- Revenue distribution

## Features

- **Scalable Infrastructure**: Handles growing computational needs
- **Fair Distribution**: Equitable value routing
- **Real-time Processing**: Immediate dividend calculations
- **Resource Optimization**: Efficient compute allocation
- **Transparent Tracking**: Clear usage and value attribution

## Getting Started

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your credentials
```

3. Run tests:
```bash
pytest tests/grid/
```

## Architecture

The Grid operates on these principles:
1. **Efficiency**: Optimal resource utilization
2. **Fairness**: Equitable value distribution
3. **Transparency**: Clear attribution and tracking
4. **Scalability**: Handles growing demands

## System Components

### Compute Layer
- Container orchestration
- Resource management
- Performance monitoring
- Auto-scaling

### Dividend Engine
- Value calculation
- Attribution tracking
- Payment processing
- Distribution logic

## 🧩 Value Calculation, Schema Registry, and Extensibility

The Grid powers dynamic value routing and dividend calculation using a robust model:
- **Demand**: How many requests exist for a data type?
- **Rarity**: Is the data common or unique?
- **Completeness/Quality**: How detailed and well-structured is the data?
- **Freshness**: Is the data recent?
- **Signal Density**: Richness of behavioral/emotional/other signals
- **Streaks & Decay**: Consistent uploads are rewarded, outdated data loses value

Grid interacts with the `schema_registry` to:
- Support new data types and value flows without code changes
- Attribute value and route dividends for any schema-aligned entry

This extensible design ensures the system can adapt to new data sources, value models, and market dynamics as Y evolves.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

## License

MIT
