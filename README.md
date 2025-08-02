# Lang Project

[![CI](https://github.com/Siddhant021295/langchain-understanding/actions/workflows/ci.yml/badge.svg)](https://github.com/Siddhant021295/langchain-understanding/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Poetry](https://img.shields.io/badge/dependency%20manager-poetry-blue)](https://python-poetry.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a Python project using Poetry for dependency management, LangChain for AI/LLM functionality, and OpenAI for GPT model integration.

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/Siddhant021295/langchain-understanding.git
cd langchain-understanding

# Install dependencies
poetry install

# Configure environment
cp .env.template .env
# Edit .env and add your OPENAI_API_KEY

# Run the project
poetry run python -m lang
```

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

## 📁 Project Structure

```
langchain-understanding/
├── .env.template          # Environment variables template
├── .github/
│   └── workflows/
│       └── ci.yml         # GitHub Actions CI/CD
├── lang/                  # Main package
│   ├── __init__.py        # Package initialization
│   ├── __main__.py        # Main application entry point
│   ├── config.py          # Configuration management
│   └── example.py         # LangChain + OpenAI integration example
├── LICENSE                # MIT License
├── README.md              # This file
├── CONTRIBUTING.md        # Contribution guidelines
├── pyproject.toml         # Poetry configuration
└── poetry.lock            # Dependency lock file
```

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
