"""Command-line interface for math validation."""

import argparse
import json
import sys
from typing import Optional

from maths_mining import MathValidator, ValidationRequest
from maths_mining.config import config


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Validate mathematical expressions using agentic requests"
    )
    parser.add_argument(
        "expression",
        help="Mathematical expression to validate (e.g., '2 + 2 = 4')"
    )
    parser.add_argument(
        "--expected",
        "-e",
        help="Expected result for validation"
    )
    parser.add_argument(
        "--context",
        "-c",
        help="Additional context for validation"
    )
    parser.add_argument(
        "--no-agent",
        action="store_true",
        help="Disable agentic validation (use basic mode)"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output result as JSON"
    )
    parser.add_argument(
        "--api-key",
        help="OpenAI API key (overrides environment variable)"
    )
    parser.add_argument(
        "--model",
        help="Model to use for agentic validation (default: gpt-4)"
    )
    
    args = parser.parse_args()
    
    # Check configuration
    use_agent = not args.no_agent
    if use_agent and not config.is_configured() and not args.api_key:
        print("Error: Agentic validation requires OpenAI API key.", file=sys.stderr)
        print("Set OPENAI_API_KEY environment variable or use --api-key option.", file=sys.stderr)
        print("Or use --no-agent flag for basic validation mode.", file=sys.stderr)
        sys.exit(1)
    
    try:
        # Create validator
        validator = MathValidator(
            use_agent=use_agent,
            api_key=args.api_key,
            model=args.model
        )
        
        # Create validation request
        request = ValidationRequest(
            expression=args.expression,
            expected_result=args.expected,
            context=args.context
        )
        
        # Perform validation
        result = validator.validate(request)
        
        # Output result
        if args.json:
            print(json.dumps(result.model_dump(), indent=2))
        else:
            print_result(result)
        
        # Exit with appropriate code
        sys.exit(0 if result.is_valid else 1)
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(2)


def print_result(result):
    """Pretty print validation result."""
    print("\n" + "=" * 60)
    print("Math Validation Result")
    print("=" * 60)
    
    status_emoji = {
        "valid": "✓",
        "invalid": "✗",
        "uncertain": "?",
        "error": "!"
    }
    
    emoji = status_emoji.get(result.status.value, "?")
    print(f"\nStatus: {emoji} {result.status.value.upper()}")
    print(f"Valid: {result.is_valid}")
    print(f"Confidence: {result.confidence:.2%}")
    print(f"\nMessage: {result.message}")
    
    if result.computed_result is not None:
        print(f"\nComputed Result: {result.computed_result}")
    
    if result.steps:
        print("\nValidation Steps:")
        for i, step in enumerate(result.steps, 1):
            print(f"  {i}. {step}")
    
    print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    main()
