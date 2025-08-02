# Lang Project

This is a Python project using Poetry for dependency management, LangChain for AI/LLM functionality, and OpenAI for GPT model integration.

## Dependencies

- **LangChain**: Framework for developing applications with language models
- **OpenAI**: Official OpenAI Python library for GPT models
- **LangChain-OpenAI**: Integration package for LangChain and OpenAI
- **Python-dotenv**: For loading environment variables from .env files
- **Python**: >=3.11,<4.0

## Environment Configuration

The project uses a `.env` file to store sensitive information like API keys:

- `.env.template`: Template file with example configuration
- `.env`: Your actual configuration (not tracked by Git)
- `lang/config.py`: Configuration management module

### Required Environment Variables:
- `OPENAI_API_KEY`: Your OpenAI API key for GPT models
- `OPENAI_ORG_ID`: (Optional) Your OpenAI organization ID

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

4. Configure your environment variables:
   ```bash
   # Copy the template to create your .env file
   cp .env.template .env
   
   # Edit .env and add your API keys
   # OPENAI_API_KEY=your-actual-api-key-here
   ```

5. (Alternative) Set environment variables directly:
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
