#!/usr/bin/python3

"""
This file defines the BaseModel class
"""
import uuid
from datetime import datetime

class BaseModel:
    """Base class for all our classes"""

    def __init__(self):
        """Initialize a new instance of the class"""
        # Generate a unique ID for the instance
        self.id = str(uuid.uuid4())
        # Set the creation and update timestamps to the current time
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """Update the update timestamp"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Convert the instance to a dictionary"""
        # Create a copy of the instance's attributes
        inst_dict = self.__dict__.copy()
        # Add the class name to the dictionary
        inst_dict["__class__"] = self.__class__.__name__
        # Convert the timestamps to ISO format
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()

        return inst_dict

    def __str__(self):
        """Return a string representation of the instance"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

if __name__ == "__main__":
    # Create a new instance of the BaseModel class
    my_model = BaseModel()
    # Set some additional attributes
    my_model.name = "My_First_Model"
    my_model.my_number = 89

    # Print the instance's ID and string representation
    print(my_model.id)
    print(my_model)

    # Print the type of the creation timestamp
    print(type(my_model.created_at))

    # Convert the instance to a dictionary and print it
    my_model_json = my_model.to_dict()
    print(my_model_json)

    # Print the dictionary's keys and values
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
