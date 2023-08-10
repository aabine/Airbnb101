import uuid
from datetime import datetime

class BaseModel:
    """A base class for all models in our hbnb clone."""
    
    def __init__(self, *args, **kwargs):
        """Initialize a new model."""

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                            setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
        elif key != "__class__":
            setattr(self, key, value)
            
        current_time = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = current_time
        self.updated_at = current_time
        
    
    
    def __str__(self):
        """Return string representation of BaseModel."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """Updates updated_at with current time when instance is changed."""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """Return dictionary representation of BaseModel."""
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result

