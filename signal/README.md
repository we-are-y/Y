# 🎯 Signal Layer

The Signal Layer is responsible for processing raw data inputs into structured, valuable signals that can be used by the Vault and Echo systems.

## Components

### Processors
- Spotify data processor
- Gmail data processor
- Rewind data processor
- Custom data processors

### Embeddings
- OpenAI embeddings integration
- Custom transformer models
- Vector storage and retrieval

### Quality Scoring
- Data quality assessment
- Signal weighting
- Confidence scoring

## 🧩 Schema Registration & Extensibility

The Signal Layer is fully extensible via the **schema registry**. Each processor:
- Registers new data types and their schemas in the `schema_registry` table (fields, units, display names, etc.)
- Maps raw data to schema-aligned entries, ensuring all data is structured and versioned
- Enables the Vault, Echo, and dashboard to adapt automatically to new data types

This design allows new processors and data sources to be added without breaking the system or requiring code changes elsewhere.

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
pytest tests/signal/
```

## Architecture

The Signal Layer follows a modular architecture where each processor:
1. Ingests raw data
2. Transforms it into a standardized format
3. Generates embeddings
4. Scores quality
5. Outputs structured signals

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

## License

MIT
