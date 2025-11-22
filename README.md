# Maths-Mining

Mining Mathematics to solve problems using agentic validation.

## Overview

Maths-Mining is a system that validates mathematical expressions and problems using agentic requests powered by AI. It combines traditional computational validation with intelligent agentic analysis to provide comprehensive mathematical validation.

## Features

- **Agentic Validation**: Uses AI (LLM) to validate mathematical expressions with detailed explanations
- **Fallback Mode**: Basic validation using SymPy when API key is not available
- **Multiple Validation Types**: 
  - Equation validation (e.g., `2 + 2 = 4`)
  - Expression evaluation (e.g., `3 * 4 + 5`)
  - Expected result comparison
- **Detailed Results**: Provides step-by-step validation process and confidence scores
- **CLI Interface**: Easy-to-use command-line interface
- **Python API**: Programmatic access for integration

## Installation

1. Clone the repository:
```bash
git clone https://github.com/DiegoLopezInc/Maths-Mining.git
cd Maths-Mining
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment (for agentic validation):
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

## Usage

### Command Line Interface

Basic equation validation:
```bash
python -m maths_mining.cli "2 + 2 = 4"
```

With expected result:
```bash
python -m maths_mining.cli "10 / 2" --expected 5
```

With context:
```bash
python -m maths_mining.cli "sqrt(16) = 4" --context "Square root validation"
```

Without agentic validation (basic mode):
```bash
python -m maths_mining.cli "3 * 3 = 9" --no-agent
```

JSON output:
```bash
python -m maths_mining.cli "5 + 5 = 10" --json
```

### Python API

```python
from maths_mining import MathValidator, ValidationRequest

# Create validator (with agentic validation)
validator = MathValidator(use_agent=True)

# Validate an equation
result = validator.validate_expression("2 + 2 = 4")
print(f"Valid: {result.is_valid}")
print(f"Message: {result.message}")
print(f"Confidence: {result.confidence}")

# Using ValidationRequest object
request = ValidationRequest(
    expression="10 / 2 = 5",
    expected_result=5,
    context="Division test"
)
result = validator.validate(request)

# Basic mode (no API key required)
validator = MathValidator(use_agent=False)
result = validator.validate_expression("3 * 4 = 12")
```

## Architecture

The system consists of several key components:

1. **Models** (`models.py`): Data models for requests and results
2. **Validator** (`validator.py`): Main validation logic with fallback mode
3. **Agent** (`agent.py`): LLM-based agentic validation
4. **Config** (`config.py`): Configuration management
5. **CLI** (`cli.py`): Command-line interface

## Configuration

Environment variables (`.env` file):

- `OPENAI_API_KEY`: Your OpenAI API key (required for agentic validation)
- `OPENAI_MODEL`: Model to use (default: `gpt-4`)
- `TEMPERATURE`: Temperature for generation (default: `0.1`, range: 0.0-1.0)

## Testing

Run tests with pytest:

```bash
pytest
```

Run specific test file:
```bash
pytest tests/test_validator.py
```

Run with verbose output:
```bash
pytest -v
```

## Examples

### Valid Equation
```python
validator = MathValidator(use_agent=False)
result = validator.validate_expression("2 + 2 = 4")
# Result: is_valid=True, status=VALID
```

### Invalid Equation
```python
validator = MathValidator(use_agent=False)
result = validator.validate_expression("2 + 2 = 5")
# Result: is_valid=False, status=INVALID
```

### Complex Expression
```python
validator = MathValidator(use_agent=False)
result = validator.validate_expression("(5 + 3) * 2 = 16")
# Result: is_valid=True, computed_result={'left': 16, 'right': 16}
```

### With Expected Result
```python
validator = MathValidator(use_agent=False)
result = validator.validate_expression("sqrt(25)", expected_result=5)
# Result: is_valid=True, computed_result=5.0
```

## API Reference

### MathValidator

Main validator class.

**Methods:**
- `__init__(use_agent=True, api_key=None, model=None)`: Initialize validator
- `validate(request: ValidationRequest) -> ValidationResult`: Validate using request object
- `validate_expression(expression, expected_result=None, context=None) -> ValidationResult`: Validate expression directly

### ValidationRequest

Request model for validation.

**Fields:**
- `expression` (str): Mathematical expression to validate
- `expected_result` (Optional[Any]): Expected result
- `context` (Optional[str]): Additional context

### ValidationResult

Result model from validation.

**Fields:**
- `status` (ValidationStatus): Validation status (VALID, INVALID, UNCERTAIN, ERROR)
- `is_valid` (bool): Whether expression is valid
- `message` (str): Explanation message
- `computed_result` (Optional[Any]): Computed result
- `steps` (Optional[List[str]]): Validation steps
- `confidence` (float): Confidence score (0.0-1.0)
- `metadata` (Optional[Dict]): Additional metadata

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.
