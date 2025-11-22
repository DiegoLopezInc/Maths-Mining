"""Agentic validation using LLM."""

from typing import Optional, Dict, Any
import json
from openai import OpenAI

from maths_mining.config import config
from maths_mining.models import ValidationStatus, ValidationResult


class MathValidationAgent:
    """Agent that uses LLM to validate mathematical expressions."""
    
    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        """Initialize the validation agent.
        
        Args:
            api_key: OpenAI API key (uses config if not provided)
            model: Model to use (uses config if not provided)
        """
        self.api_key = api_key or config.OPENAI_API_KEY
        self.model = model or config.OPENAI_MODEL
        
        if not self.api_key:
            raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY environment variable.")
        
        self.client = OpenAI(api_key=self.api_key)
    
    def validate(
        self, 
        expression: str, 
        expected_result: Optional[Any] = None,
        context: Optional[str] = None
    ) -> ValidationResult:
        """Validate a mathematical expression using the agent.
        
        Args:
            expression: The mathematical expression to validate
            expected_result: Expected result if known
            context: Additional context for validation
            
        Returns:
            ValidationResult with validation details
        """
        try:
            prompt = self._build_prompt(expression, expected_result, context)
            response = self._call_llm(prompt)
            return self._parse_response(response, expression)
        except Exception as e:
            return ValidationResult(
                status=ValidationStatus.ERROR,
                is_valid=False,
                message=f"Error during validation: {str(e)}",
                confidence=0.0
            )
    
    def _build_prompt(
        self, 
        expression: str, 
        expected_result: Optional[Any],
        context: Optional[str]
    ) -> str:
        """Build the prompt for the LLM."""
        prompt = f"""You are a mathematical validation expert. Your task is to validate mathematical expressions and problems.

Expression to validate: {expression}
"""
        
        if expected_result is not None:
            prompt += f"Expected result: {expected_result}\n"
        
        if context:
            prompt += f"Context: {context}\n"
        
        prompt += """
Please validate this mathematical expression and provide your response in the following JSON format:
{
    "is_valid": true/false,
    "message": "Explanation of why the expression is valid or invalid",
    "computed_result": "The computed result if applicable (or null)",
    "steps": ["Step 1", "Step 2", ...],
    "confidence": 0.0-1.0
}

Focus on:
1. Mathematical correctness
2. Proper notation and syntax
3. Logical consistency
4. Computational accuracy

Respond ONLY with the JSON object, no additional text."""
        
        return prompt
    
    def _call_llm(self, prompt: str) -> str:
        """Call the LLM with the prompt."""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a precise mathematical validation expert. Always respond with valid JSON."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=config.TEMPERATURE,
            max_tokens=1000
        )
        
        return response.choices[0].message.content
    
    def _parse_response(self, response: str, expression: str) -> ValidationResult:
        """Parse the LLM response into a ValidationResult."""
        try:
            # Extract JSON from response
            response = response.strip()
            if response.startswith("```json"):
                response = response[7:]
            if response.startswith("```"):
                response = response[3:]
            if response.endswith("```"):
                response = response[:-3]
            response = response.strip()
            
            data = json.loads(response)
            
            is_valid = data.get("is_valid", False)
            status = ValidationStatus.VALID if is_valid else ValidationStatus.INVALID
            
            return ValidationResult(
                status=status,
                is_valid=is_valid,
                message=data.get("message", "No message provided"),
                computed_result=data.get("computed_result"),
                steps=data.get("steps"),
                confidence=float(data.get("confidence", 0.0)),
                metadata={"expression": expression}
            )
        except json.JSONDecodeError as e:
            return ValidationResult(
                status=ValidationStatus.UNCERTAIN,
                is_valid=False,
                message=f"Could not parse validation response: {str(e)}",
                confidence=0.0,
                metadata={"raw_response": response}
            )
        except Exception as e:
            return ValidationResult(
                status=ValidationStatus.ERROR,
                is_valid=False,
                message=f"Error parsing response: {str(e)}",
                confidence=0.0
            )
