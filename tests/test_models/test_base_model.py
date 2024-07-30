#!/usr/bin/python3

"""
Module for BaseModel unittest
"""
import unittest
from models.base_model import BaseModel

class TestBasemodel(unittest.TestCase):
    """
    Unittest for BaseModel
    """

    def test_init(self):
        """
        Test the initialization of a new BaseModel instance
        """
        # Create a new instance of BaseModel
        my_model = BaseModel()

        # Check if the instance has an ID, creation timestamp, and update timestamp
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        """
        Test the save method of BaseModel
        """
        # Create a new instance of BaseModel
        my_model = BaseModel()

        # Store the initial update timestamp
        initial_updated_at = my_model.updated_at

        # Call the save method and store the new update timestamp
        current_updated_at = my_model.save()

        # Check if the update timestamp has changed
        self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of BaseModel
        """
        # Create a new instance of BaseModel
        my_model = BaseModel()

        # Convert the instance to a dictionary
        my_model_dict = my_model.to_dict()

        # Check if the result is a dictionary
        self.assertIsInstance(my_model_dict, dict)

        # Check if the dictionary contains the correct class name, ID, creation timestamp, and update timestamp
        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict["updated_at"], my_model.updated_at.isoformat())

    def test_str(self):
        """
        Test the string representation of BaseModel
        """
        # Create a new instance of BaseModel
        my_model = BaseModel()

        # Check if the string representation starts with the class name
        self.assertTrue(str(my_model).startswith('[BaseModel]'))

        # Check if the string representation contains the instance's ID and attributes
        self.assertIn(my_model.id, str(my_model))
        self.assertIn(str(my_model.__dict__), str(my_model))

if __name__ == "__main__":
    # Run the unittests
    unittest.main()
