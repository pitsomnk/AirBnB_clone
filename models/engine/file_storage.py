#!/usr/bin/python3
"""
Module for serializing and deserializing data
"""
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """
    FileStorage class for storing, serializing and deserializing data
    """
    # Private class variables to store the file path and objects
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        Adds a new object to the __objects dictionary with a key of
        <obj class name>.id.
        """
        # Get the class name of the object
        obj_cls_name = obj.__class__.__name__

        # Create a key for the object using the class name and ID
        key = "{}.{}".format(obj_cls_name, obj.id)

        # Store the object in the __objects dictionary
        FileStorage.__objects[key] = obj

    def all(self):
        """
        Returns the __objects dictionary, providing access to all stored objects.
        """
        return FileStorage.__objects

    def save(self):
        """
        Serializes the __objects dictionary to JSON format and saves it to the file.
        """
        # Get all objects from the __objects dictionary
        all_objs = FileStorage.__objects

        # Create a dictionary to store the objects in a serializable format
        obj_dict = {}

        # Iterate over the objects and convert them to dictionaries using the to_dict method
        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()

        # Open the file in write mode and dump the JSON data
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file and loads the data into the __objects dictionary.
        """
        # Check if the file exists
        if os.path.isfile(FileStorage.__file_path):
            # Open the file in read mode
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    # Load the JSON data from the file
                    obj_dict = json.load(file)

                    # Iterate over the objects in the JSON data
                    for key, value in obj_dict.items():
                        # Split the key into class name and object ID
                        class_name, obj_id = key.split('.')

                        # Get the class using the class name
                        cls = eval(class_name)

                        # Create a new instance of the class using the dictionary data
                        instance = cls(**value)

                        # Store the instance in the __objects dictionary
                        FileStorage.__objects[key] = instance
                except Exception:
                    # Ignore any exceptions that occur during deserialization
                    pass
