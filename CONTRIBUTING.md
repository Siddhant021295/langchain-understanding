# Contributing to Lang Project

Thank you for your interest in contributing to this project! Here are some guidelines to help you get started.

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a new branch for your feature/fix
4. Make your changes
5. Test your changes
6. Submit a pull request

## Development Setup

1. Install Poetry:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Clone and setup:
   ```bash
   git clone https://github.com/Siddhant021295/langchain-understanding.git
   cd langchain-understanding
   poetry install
   ```

3. Configure environment:
   ```bash
   cp .env.template .env
   # Edit .env with your API keys
   ```

4. Run tests:
   ```bash
   poetry run python -m lang
   poetry run python -m lang.example
   ```

## Code Style

- Follow PEP 8 Python style guidelines
- Use type hints where appropriate
- Add docstrings to functions and classes
- Keep functions focused and modular

## Commit Messages

Use clear, descriptive commit messages:
- `feat: add new feature`
- `fix: resolve bug in module`
- `docs: update README`
- `refactor: improve code structure`

## Pull Request Process

1. Update documentation if needed
2. Add tests for new functionality
3. Ensure all tests pass
4. Update the README if needed
5. Submit PR with clear description

## Questions?

Feel free to open an issue for questions or discussions!
