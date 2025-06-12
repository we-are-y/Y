# 🔑 API Layer

The API Layer manages access control, monetization, and enterprise integration for the Y system.

## Components

### Access Control
- Gatekeeper agents
- Consent management
- Permission verification
- Rate limiting
- Usage tracking

### Monetization
- Royalty calculation
- Usage tracking
- Payout processing
- Value attribution
- Revenue sharing

## Features

- **Granular Permissions**: Fine-grained access control
- **Consent Management**: User-controlled data sharing
- **Usage Tracking**: Detailed analytics and reporting
- **Monetization**: Fair value distribution
- **Enterprise Integration**: Business-ready APIs

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
pytest tests/api_layer/
```

## API Documentation

### Access Control Endpoints
- `POST /api/v1/consent`: Manage data sharing consent
- `GET /api/v1/permissions`: Check current permissions
- `POST /api/v1/revoke`: Revoke access

### Monetization Endpoints
- `GET /api/v1/royalties`: View earned royalties
- `POST /api/v1/payout`: Request payout
- `GET /api/v1/usage`: View usage statistics

## Architecture

The API Layer follows these principles:
1. **Security First**: All requests are authenticated and authorized
2. **Transparency**: Clear consent and usage tracking
3. **Fair Value**: Equitable monetization for all participants

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

## License

MIT

## 🧩 Human & Enterprise APIs, Extensibility, and Schema Registry

The API Layer supports both **Human API** (for accessing individual user Vaults with consent) and **Enterprise API** (for business-to-business data access, e.g., enterprise data from platforms like Tesla or Deliveroo).

- All data requests and permissions are schema-driven, leveraging the dynamic `schema_registry` for extensibility.
- New types of data requests and complex criteria matching can be supported without code changes—just by registering new schemas and request types.
- The API Layer is designed to be future-proof, adapting to new data types, requesters, and value flows as the ecosystem grows. 