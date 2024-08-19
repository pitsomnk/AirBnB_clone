# Import the FileStorage class from the models.engine.file_storage module
from models.engine.file_storage import FileStorage

# Create an instance of the FileStorage class, which will be used to store and manage data
storage = FileStorage()

# Call the reload method of the FileStorage instance, which will reload the data from the storage file
# This is likely used to refresh the data in memory with the latest data from the file
storage.reload()
