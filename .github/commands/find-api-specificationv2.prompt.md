# API & Integration Specification Discovery

## Objective
Analyze the codebase and document all API specifications and integration entry points **received/consumed/incoming** by this application.

## Scope of Analysis

### 1. HTTP/REST API Endpoints
- All routes/endpoints that receive incoming HTTP requests
- Include: method, path, query params, headers, request/response body schema

### 2. GraphQL
- Queries, Mutations, and Subscriptions exposed by the application
- Include: schema definitions, resolvers location

### 3. WebSocket Endpoints
- WebSocket connection handlers
- Event listeners and message handlers

### 4. gRPC Services
- Proto definitions implemented by this application
- Service methods and their handlers

### 5. Message Broker Consumers
- **Kafka**: Topics consumed, consumer group configurations
- **RabbitMQ**: Queues consumed, exchange bindings
- **AWS SQS/SNS**: Queue listeners, topic subscriptions
- **Redis Pub/Sub**: Channel subscriptions
- **Google Pub/Sub**: Subscription handlers

### 6. Scheduled Jobs / Cron Tasks
- Cron expressions and their handlers
- Scheduled task definitions (e.g., @Scheduled, node-cron, celery beat)

### 7. Webhooks (Incoming)
- Webhook receiver endpoints
- Payload validation and processing logic

### 8. Event-Driven Handlers
- Internal event listeners/subscribers
- Domain event handlers

### 9. CLI Commands
- Command-line interface entry points
- Artisan/management commands (Laravel, Django, etc.)

### 10. File/Directory Watchers
- File system event listeners
- Hot-reload or file processing triggers

---

## Output Format

For each discovered integration, provide documentation in this structure:

```
# {Integration Type}: {Name/Identifier}

## Description

## Sample Request

## Sample Response (if applicable)

## Code Entry Point
\`\`\`{relative-path-file}:{start-line}-{end-line}
\`\`\`
```