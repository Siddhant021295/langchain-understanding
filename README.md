# Lang Project

This is a Python project using Poetry for dependency management, LangChain for AI/LLM functionality, and OpenAI for GPT model integration.

## Dependencies

- **LangChain**: Framework for developing applications with language models
- **OpenAI**: Official OpenAI Python library for GPT models
- **Python**: >=3.11,<4.0

## Setup

1. Install Poetry if you haven't already:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

4. (Optional) Set your OpenAI API key for actual API calls:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

## Development

To add new dependencies:
```bash
poetry add package_name
```

To add development dependencies:
```bash
poetry add --group dev package_name
```

## Running the project

```bash
poetry run python -m lang
```

## AI/LLM Integration

The project includes:
- **LangChain**: For building AI applications and chaining language model operations
- **OpenAI**: For accessing GPT models and other OpenAI services

The main module demonstrates basic integration of both libraries.
