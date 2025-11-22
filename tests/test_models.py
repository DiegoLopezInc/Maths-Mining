"""Tests for data models."""

import pytest
from maths_mining.models import (
    ValidationRequest,
    ValidationResult,
    ValidationStatus
)


class TestValidationRequest:
    """Tests for ValidationRequest model."""
    
    def test_create_basic_request(self):
        """Test creating a basic validation request."""
        request = ValidationRequest(expression="2 + 2")
        assert request.expression == "2 + 2"
        assert request.expected_result is None
        assert request.context is None
    
    def test_create_full_request(self):
        """Test creating a full validation request."""
        request = ValidationRequest(
            expression="2 + 2 = 4",
            expected_result=4,
            context="Simple arithmetic"
        )
        assert request.expression == "2 + 2 = 4"
        assert request.expected_result == 4
        assert request.context == "Simple arithmetic"
    
    def test_request_validation(self):
        """Test that request requires expression."""
        with pytest.raises(Exception):
            ValidationRequest()


class TestValidationResult:
    """Tests for ValidationResult model."""
    
    def test_create_valid_result(self):
        """Test creating a valid result."""
        result = ValidationResult(
            status=ValidationStatus.VALID,
            is_valid=True,
            message="Expression is correct",
            confidence=0.95
        )
        assert result.status == ValidationStatus.VALID
        assert result.is_valid is True
        assert result.message == "Expression is correct"
        assert result.confidence == 0.95
    
    def test_create_invalid_result(self):
        """Test creating an invalid result."""
        result = ValidationResult(
            status=ValidationStatus.INVALID,
            is_valid=False,
            message="Expression is incorrect",
            computed_result=5,
            confidence=0.9
        )
        assert result.status == ValidationStatus.INVALID
        assert result.is_valid is False
        assert result.computed_result == 5
    
    def test_result_with_steps(self):
        """Test result with validation steps."""
        result = ValidationResult(
            status=ValidationStatus.VALID,
            is_valid=True,
            message="Validated successfully",
            steps=["Step 1", "Step 2", "Step 3"],
            confidence=0.99
        )
        assert len(result.steps) == 3
        assert result.steps[0] == "Step 1"
    
    def test_confidence_range(self):
        """Test that confidence is within valid range."""
        # Valid confidence values
        result = ValidationResult(
            status=ValidationStatus.VALID,
            is_valid=True,
            message="Test",
            confidence=0.5
        )
        assert 0.0 <= result.confidence <= 1.0
        
        # Test boundary values
        result = ValidationResult(
            status=ValidationStatus.VALID,
            is_valid=True,
            message="Test",
            confidence=0.0
        )
        assert result.confidence == 0.0
        
        result = ValidationResult(
            status=ValidationStatus.VALID,
            is_valid=True,
            message="Test",
            confidence=1.0
        )
        assert result.confidence == 1.0


class TestValidationStatus:
    """Tests for ValidationStatus enum."""
    
    def test_status_values(self):
        """Test all status enum values."""
        assert ValidationStatus.VALID == "valid"
        assert ValidationStatus.INVALID == "invalid"
        assert ValidationStatus.UNCERTAIN == "uncertain"
        assert ValidationStatus.ERROR == "error"
