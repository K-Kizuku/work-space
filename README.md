# Meeting Advisor Service

This repository contains a simple gRPC microservice that uses LangChain and VertexAI to provide real-time meeting advice based on meeting transcripts.

## Development Environment

A [devcontainer](https://containers.dev/) configuration is provided. It installs dependencies using the `uv` package manager and includes `mypy` for type checking.

## Usage

1. Build and start the devcontainer in your IDE.
2. Inside the container, run the gRPC server:

```bash
python server.py
```

3. In another terminal, execute the sample client to send a test transcript:

```bash
python client.py
```

The client will output generated advice.

## Type Checking

Run `mypy` to check types:

```bash
mypy .
```
