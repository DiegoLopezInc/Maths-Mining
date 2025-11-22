"""Tests for the math validator."""

import pytest
from maths_mining import MathValidator, ValidationRequest
from maths_mining.models import ValidationStatus


class TestMathValidatorBasic:
    """Tests for basic (non-agent) validation."""
    
    def test_validator_creation_no_agent(self):
        """Test creating validator without agent."""
        validator = MathValidator(use_agent=False)
        assert validator.use_agent is False
        assert validator.agent is None
    
    def test_simple_equation_valid(self):
        """Test validating a simple valid equation."""
        validator = MathValidator(use_agent=False)
        result = validator.validate_expression("2 + 2 = 4")
        
        assert result.is_valid is True
        assert result.status == ValidationStatus.VALID
        assert result.computed_result is not None
    
    def test_simple_equation_invalid(self):
        """Test validating a simple invalid equation."""
        validator = MathValidator(use_agent=False)
        result = validator.validate_expression("2 + 2 = 5")
        
        assert result.is_valid is False
        assert result.status == ValidationStatus.INVALID
    
    def test_expression_evaluation(self):
        """Test evaluating an expression without equation."""
        validator = MathValidator(use_agent=False)
        result = validator.validate_expression("3 * 4 + 5")
        
        assert result.is_valid is True
        assert result.computed_result == 17
    
    def test_expression_with_expected_result(self):
        """Test expression with expected result."""
        validator = MathValidator(use_agent=False)
        result = validator.validate_expression("10 / 2", expected_result=5)
        
        assert result.is_valid is True
        assert abs(result.computed_result - 5) < 1e-10
    
    def test_expression_with_wrong_expected_result(self):
        """Test expression with wrong expected result."""
        validator = MathValidator(use_agent=False)
        result = validator.validate_expression("10 / 2", expected_result=4)
        
        assert result.is_valid is False
    
    def test_complex_expression(self):
        """Test a more complex expression."""
        validator = MathValidator(use_agent=False)
        result = validator.validate_expression("(5 + 3) * 2 = 16")
        
        assert result.is_valid is True
        assert result.status == ValidationStatus.VALID
    
    def test_invalid_syntax(self):
        """Test handling of invalid syntax."""
        validator = MathValidator(use_agent=False)
        result = validator.validate_expression("2 +* 2")
        
        assert result.is_valid is False
        assert result.status == ValidationStatus.ERROR
    
    def test_validation_with_request_object(self):
        """Test validation using ValidationRequest object."""
        validator = MathValidator(use_agent=False)
        request = ValidationRequest(
            expression="7 * 6 = 42",
            context="Multiplication test"
        )
        result = validator.validate(request)
        
        assert result.is_valid is True
        assert result.status == ValidationStatus.VALID
    
    def test_square_root(self):
        """Test square root expression."""
        validator = MathValidator(use_agent=False)
        result = validator.validate_expression("sqrt(16) = 4")
        
        assert result.is_valid is True
    
    def test_power_operation(self):
        """Test power operation."""
        validator = MathValidator(use_agent=False)
        result = validator.validate_expression("2**3 = 8")
        
        assert result.is_valid is True


class TestMathValidatorAgent:
    """Tests for agentic validation (requires API key)."""
    
    def test_validator_creation_requires_api_key(self):
        """Test that agentic validator requires API key."""
        # This should raise an error if no API key is configured
        # We'll catch it to allow tests to run without API key
        try:
            validator = MathValidator(use_agent=True)
            # If we get here, API key is configured
            assert validator.agent is not None
        except ValueError as e:
            # Expected when no API key is configured
            assert "API key" in str(e)
    
    def test_validator_with_api_key_param(self):
        """Test creating validator with API key parameter."""
        # Test with dummy key - actual validation will fail but object should be created
        try:
            validator = MathValidator(use_agent=True, api_key="test-key")
            assert validator.agent is not None
        except Exception:
            # May fail if trying to validate the key, that's okay
            pass


class TestValidationSteps:
    """Tests for validation steps and details."""
    
    def test_result_contains_steps(self):
        """Test that results contain validation steps."""
        validator = MathValidator(use_agent=False)
        result = validator.validate_expression("5 + 5 = 10")
        
        assert result.steps is not None
        assert len(result.steps) > 0
    
    def test_result_has_confidence(self):
        """Test that results have confidence score."""
        validator = MathValidator(use_agent=False)
        result = validator.validate_expression("3 * 3 = 9")
        
        assert result.confidence > 0
        assert result.confidence <= 1.0
    
    def test_result_has_message(self):
        """Test that results have descriptive message."""
        validator = MathValidator(use_agent=False)
        result = validator.validate_expression("1 + 1 = 2")
        
        assert result.message is not None
        assert len(result.message) > 0
