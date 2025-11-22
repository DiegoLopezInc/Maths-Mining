"""Data models for math validation."""

from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from enum import Enum


class ValidationStatus(str, Enum):
    """Status of validation result."""
    VALID = "valid"
    INVALID = "invalid"
    UNCERTAIN = "uncertain"
    ERROR = "error"


class ValidationRequest(BaseModel):
    """Request model for math validation."""
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "expression": "2 + 2 = 4",
                "expected_result": 4,
                "context": "Simple arithmetic validation"
            }
        }
    )
    
    expression: str = Field(..., description="The mathematical expression or problem to validate")
    expected_result: Optional[Any] = Field(None, description="Expected result if known")
    context: Optional[str] = Field(None, description="Additional context for validation")


class ValidationResult(BaseModel):
    """Result model for math validation."""
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "status": "valid",
                "is_valid": True,
                "message": "The expression is mathematically correct",
                "computed_result": 4,
                "steps": ["Parse expression", "Evaluate", "Compare with expected"],
                "confidence": 0.99,
                "metadata": {}
            }
        }
    )
    
    status: ValidationStatus = Field(..., description="Validation status")
    is_valid: bool = Field(..., description="Whether the expression is mathematically valid")
    message: str = Field(..., description="Explanation of the validation result")
    computed_result: Optional[Any] = Field(None, description="Computed result if applicable")
    steps: Optional[List[str]] = Field(None, description="Step-by-step validation process")
    confidence: float = Field(0.0, ge=0.0, le=1.0, description="Confidence score of validation")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Additional metadata")
