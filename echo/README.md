# 🤖 Echo

Echo is your personal AI agent that knows you better than anyone. It grows with you, protects you, and speaks as you, not just for you.

## Components

### Memory
- Long-term memory storage
- Memory retrieval and indexing
- Context management
- Memory pruning and optimization

### Prompts
- Role behavior templates
- Conversation patterns
- Personality traits
- Response formatting

### Routing
- Agent interaction logic
- Decision making
- Task prioritization
- Context switching

## Features

- **Personal Growth**: Learns and adapts to your preferences
- **Privacy First**: All data stays in your Vault
- **Contextual Awareness**: Maintains conversation history
- **Multi-modal**: Handles text, voice, and visual inputs
- **Proactive**: Anticipates needs based on patterns

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
pytest tests/echo/
```

## Architecture

Echo operates on three main principles:
1. **Memory**: Maintains a persistent, searchable record of interactions
2. **Context**: Understands and maintains conversation state
3. **Personality**: Adapts its communication style to match yours

## 🧩 Schema Registry & Dynamic Memory

Echo is fully extensible and adapts to any data type via the **schema registry**. This means:
- Echo can understand and reason about any new data type added to the Vault
- The memory layer is built from schema-aligned entries, ensuring structured, versioned, and rich context
- Prompt/response logging and per-user embedding metadata enable transparency, replay, and continuous improvement

As new schemas are registered, Echo's capabilities and insights grow automatically—no code changes required.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

## License

MIT
