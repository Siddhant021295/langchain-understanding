# Lang Project

This is a Python project using Poetry for dependency management and LangChain for AI/LLM functionality.

## Dependencies

- **LangChain**: Framework for developing applications with language models
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

## LangChain Integration

The project includes LangChain for building AI applications. The main module demonstrates basic LangChain message creation.
