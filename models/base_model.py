#!/usr/bin/python3
"""
Module base_model

This module contains the definition for the BaseModel class.
"""

import uuid
from datetime import datetime

import models

class BaseModel:
    """BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.

        Args:
            *args: Additional arguments (not used in this version).
            **kwargs (dict): Key/value pairs for attribute initialization.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        # Initialize attributes from kwargs (if provided)
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime and save to storage."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of the instance's __dict__.
        """
        base_dict = {
            key: (value.isoformat() if isinstance(value, datetime) else value)
            for key, value in self.__dict__.items()
        }
        base_dict["__class__"] = self.__class__.__name__
        return base_dict

    def __str__(self) -> str:
        """Return a string representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

