# Lang Project

This is a Python project using Poetry for dependency management.

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
