"""Basic usage examples for Maths-Mining."""

from maths_mining import MathValidator, ValidationRequest

# Example 1: Simple equation validation (basic mode)
print("=" * 60)
print("Example 1: Simple Equation Validation")
print("=" * 60)

validator = MathValidator(use_agent=False)
result = validator.validate_expression("2 + 2 = 4")

print(f"Expression: 2 + 2 = 4")
print(f"Valid: {result.is_valid}")
print(f"Status: {result.status}")
print(f"Message: {result.message}")
print(f"Confidence: {result.confidence:.2%}")
print()

# Example 2: Invalid equation
print("=" * 60)
print("Example 2: Invalid Equation")
print("=" * 60)

result = validator.validate_expression("2 + 2 = 5")

print(f"Expression: 2 + 2 = 5")
print(f"Valid: {result.is_valid}")
print(f"Status: {result.status}")
print(f"Message: {result.message}")
print()

# Example 3: Expression evaluation
print("=" * 60)
print("Example 3: Expression Evaluation")
print("=" * 60)

result = validator.validate_expression("3 * 4 + 5")

print(f"Expression: 3 * 4 + 5")
print(f"Valid: {result.is_valid}")
print(f"Computed Result: {result.computed_result}")
print(f"Message: {result.message}")
print()

# Example 4: Expression with expected result
print("=" * 60)
print("Example 4: With Expected Result")
print("=" * 60)

result = validator.validate_expression("sqrt(25)", expected_result=5)

print(f"Expression: sqrt(25)")
print(f"Expected: 5")
print(f"Valid: {result.is_valid}")
print(f"Computed Result: {result.computed_result}")
print(f"Message: {result.message}")
print()

# Example 5: Complex expression
print("=" * 60)
print("Example 5: Complex Expression")
print("=" * 60)

result = validator.validate_expression("(5 + 3) * 2 = 16")

print(f"Expression: (5 + 3) * 2 = 16")
print(f"Valid: {result.is_valid}")
print(f"Status: {result.status}")
print(f"Computed Result: {result.computed_result}")
print()

# Example 6: Using ValidationRequest object
print("=" * 60)
print("Example 6: Using ValidationRequest")
print("=" * 60)

request = ValidationRequest(
    expression="7 * 6 = 42",
    expected_result=42,
    context="Multiplication validation"
)
result = validator.validate(request)

print(f"Expression: {request.expression}")
print(f"Context: {request.context}")
print(f"Valid: {result.is_valid}")
print(f"Message: {result.message}")

if result.steps:
    print("\nValidation Steps:")
    for i, step in enumerate(result.steps, 1):
        print(f"  {i}. {step}")

print()

# Example 7: Error handling
print("=" * 60)
print("Example 7: Invalid Syntax Error Handling")
print("=" * 60)

result = validator.validate_expression("2 + + 2")

print(f"Expression: 2 + + 2")
print(f"Valid: {result.is_valid}")
print(f"Status: {result.status}")
print(f"Message: {result.message}")
print()

print("=" * 60)
print("All examples completed!")
print("=" * 60)
