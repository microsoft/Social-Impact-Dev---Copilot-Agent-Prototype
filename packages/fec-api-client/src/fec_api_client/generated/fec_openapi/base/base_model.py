"""
Base model class for all generated models.
"""

import json
from typing import Dict, Any, TypeVar, Type


T = TypeVar('T', bound='BaseModel')


class BaseModel:
    """Base class for all generated model classes with common serialization methods."""

    def __init__(self, data: Dict[str, Any] | None = None):
        """Initialize the model with optional data dictionary."""
        self._data = data or {}

    def to_dict(self) -> Dict[str, Any]:
        """Convert model to dictionary with nested object support."""
        result = {}
        for key, value in self._data.items():
            if hasattr(value, 'to_dict'):
                # Handle nested model objects
                result[key] = value.to_dict()
            elif isinstance(value, list):
                # Handle lists that might contain model objects
                result[key] = [
                    item.to_dict() if hasattr(item, "to_dict") else item for item in value
                ]
            else:
                result[key] = value
        return result

    def to_json(self) -> str:
        """Convert model to JSON string."""
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls: Type[T], data: Dict[str, Any]) -> T:
        """Create model from dictionary."""
        return cls(data)

    @classmethod
    def from_json(cls: Type[T], json_str: str) -> T:
        """Create model from JSON string."""
        return cls(json.loads(json_str))
