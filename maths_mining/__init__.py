"""Maths Mining - A system to validate math using agentic requests."""

__version__ = "0.1.0"

from maths_mining.validator import MathValidator
from maths_mining.models import ValidationRequest, ValidationResult

__all__ = ["MathValidator", "ValidationRequest", "ValidationResult"]
