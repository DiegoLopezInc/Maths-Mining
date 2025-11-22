"""Main math validator implementation."""

from typing import Optional
import sympy as sp

from maths_mining.models import ValidationRequest, ValidationResult, ValidationStatus
from maths_mining.agent import MathValidationAgent
from maths_mining.config import config


class MathValidator:
    """Main validator for mathematical expressions using agentic requests."""
    
    def __init__(
        self, 
        use_agent: bool = True,
        api_key: Optional[str] = None,
        model: Optional[str] = None
    ):
        """Initialize the math validator.
        
        Args:
            use_agent: Whether to use the agentic validation (requires API key)
            api_key: OpenAI API key (uses config if not provided)
            model: Model to use (uses config if not provided)
        """
        self.use_agent = use_agent
        self.agent = None
        
        if use_agent:
            if not config.is_configured() and not api_key:
                raise ValueError(
                    "Agentic validation requires OpenAI API key. "
                    "Set OPENAI_API_KEY environment variable or provide api_key parameter."
                )
            self.agent = MathValidationAgent(api_key=api_key, model=model)
    
    def validate(self, request: ValidationRequest) -> ValidationResult:
        """Validate a mathematical expression.
        
        Args:
            request: ValidationRequest with expression and optional expected result
            
        Returns:
            ValidationResult with validation details
        """
        if self.use_agent and self.agent:
            return self._validate_with_agent(request)
        else:
            return self._validate_basic(request)
    
    def validate_expression(
        self, 
        expression: str, 
        expected_result: Optional[any] = None,
        context: Optional[str] = None
    ) -> ValidationResult:
        """Validate a mathematical expression directly.
        
        Args:
            expression: The mathematical expression to validate
            expected_result: Expected result if known
            context: Additional context for validation
            
        Returns:
            ValidationResult with validation details
        """
        request = ValidationRequest(
            expression=expression,
            expected_result=expected_result,
            context=context
        )
        return self.validate(request)
    
    def _validate_with_agent(self, request: ValidationRequest) -> ValidationResult:
        """Validate using the agentic approach."""
        return self.agent.validate(
            expression=request.expression,
            expected_result=request.expected_result,
            context=request.context
        )
    
    def _validate_basic(self, request: ValidationRequest) -> ValidationResult:
        """Basic validation without agent (fallback mode)."""
        try:
            expression = request.expression
            
            # Try to parse and evaluate with sympy
            if "=" in expression:
                # Handle equations
                parts = expression.split("=")
                if len(parts) == 2:
                    left = sp.sympify(parts[0].strip())
                    right = sp.sympify(parts[1].strip())
                    
                    # Evaluate both sides
                    left_val = left.evalf() if hasattr(left, 'evalf') else left
                    right_val = right.evalf() if hasattr(right, 'evalf') else right
                    
                    is_valid = abs(float(left_val) - float(right_val)) < 1e-10
                    
                    return ValidationResult(
                        status=ValidationStatus.VALID if is_valid else ValidationStatus.INVALID,
                        is_valid=is_valid,
                        message=f"Equation validation: {left_val} {'==' if is_valid else '!='} {right_val}",
                        computed_result={"left": float(left_val), "right": float(right_val)},
                        steps=["Parse expression", "Evaluate left side", "Evaluate right side", "Compare"],
                        confidence=0.9 if is_valid else 0.8
                    )
            else:
                # Single expression evaluation
                expr = sp.sympify(expression)
                result = expr.evalf() if hasattr(expr, 'evalf') else expr
                
                # Check against expected result if provided
                is_valid = True
                message = f"Expression evaluated successfully: {result}"
                
                if request.expected_result is not None:
                    expected = float(request.expected_result)
                    computed = float(result)
                    is_valid = abs(computed - expected) < 1e-10
                    message = f"Result {'matches' if is_valid else 'does not match'} expected: {computed} vs {expected}"
                
                return ValidationResult(
                    status=ValidationStatus.VALID if is_valid else ValidationStatus.INVALID,
                    is_valid=is_valid,
                    message=message,
                    computed_result=float(result),
                    steps=["Parse expression", "Evaluate expression"],
                    confidence=0.9
                )
                
        except Exception as e:
            return ValidationResult(
                status=ValidationStatus.ERROR,
                is_valid=False,
                message=f"Error during validation: {str(e)}",
                confidence=0.0,
                metadata={"error": str(e)}
            )
